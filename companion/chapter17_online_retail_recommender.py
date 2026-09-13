"""Chapter 17 reference: item-item recommendation with Online Retail II.

Prepare the controlled UCI archive first:
    python companion/download_datasets.py --dataset online_retail_ii --include-large

The reference treats valid customer-product purchases as implicit feedback. It
uses a bounded top-item matrix so the baseline remains practical on a laptop;
the book's Chapter 17 lab asks readers to add chronological evaluation, ranking
metrics, cold-start analysis, and a content signal.
"""
from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


def find_workbooks(data_root: Path) -> list[Path]:
    root = data_root / "uci" / "online_retail_ii" / "raw"
    workbooks = sorted(root.rglob("*.xlsx")) + sorted(root.rglob("*.xls"))
    if not workbooks:
        raise FileNotFoundError(
            "Online Retail II workbook(s) not found. Run: "
            "python companion/download_datasets.py --dataset online_retail_ii "
            "--include-large"
        )
    return workbooks


def _resolve_column(columns: list[str], *candidates: str) -> str:
    normalized = {c.strip().lower().replace("_", " "): c for c in columns}
    for candidate in candidates:
        key = candidate.strip().lower().replace("_", " ")
        if key in normalized:
            return normalized[key]
    raise KeyError(f"required column not found; tried {candidates}; got {columns}")


def load_transactions(data_root: Path) -> tuple[pd.DataFrame, dict[str, str]]:
    frames = [pd.read_excel(path) for path in find_workbooks(data_root)]
    df = pd.concat(frames, ignore_index=True)
    columns = list(df.columns)
    resolved = {
        "invoice": _resolve_column(columns, "Invoice", "InvoiceNo"),
        "stock": _resolve_column(columns, "StockCode"),
        "description": _resolve_column(columns, "Description"),
        "quantity": _resolve_column(columns, "Quantity"),
        "customer": _resolve_column(columns, "Customer ID", "CustomerID", "Customer Id"),
    }
    return df, resolved


def clean_interactions(df: pd.DataFrame, col: dict[str, str]) -> pd.DataFrame:
    work = df.copy()
    work = work[work[col["quantity"]].fillna(0) > 0]
    invoice = work[col["invoice"]].astype(str)
    work = work[~invoice.str.startswith("C", na=False)]
    work = work.dropna(subset=[col["customer"], col["stock"]])
    work[col["customer"]] = (
        work[col["customer"]].astype(str).str.replace(r"\.0$", "", regex=True)
    )
    work[col["stock"]] = work[col["stock"]].astype(str).str.strip()
    return work


def build_item_user_matrix(
    df: pd.DataFrame,
    col: dict[str, str],
    max_items: int,
) -> pd.DataFrame:
    pairs = df[[col["customer"], col["stock"]]].drop_duplicates()
    item_support = pairs.groupby(col["stock"])[col["customer"]].nunique()
    keep = item_support.sort_values(ascending=False).head(max_items).index
    pairs = pairs[pairs[col["stock"]].isin(keep)].assign(interaction=1.0)
    customer_item = pairs.pivot_table(
        index=col["customer"],
        columns=col["stock"],
        values="interaction",
        aggfunc="max",
        fill_value=0.0,
    )
    return customer_item.T


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-root", default="data")
    parser.add_argument("--stock-code", default=None)
    parser.add_argument("--max-items", type=int, default=500)
    parser.add_argument("--top-k", type=int, default=10)
    args = parser.parse_args()

    if args.max_items < 2:
        parser.error("--max-items must be at least 2")
    if args.top_k < 1:
        parser.error("--top-k must be at least 1")

    raw, col = load_transactions(Path(args.data_root))
    clean = clean_interactions(raw, col)
    matrix = build_item_user_matrix(clean, col, args.max_items)
    if matrix.empty:
        raise RuntimeError("no valid interactions remained after cleaning")

    requested = str(args.stock_code).strip() if args.stock_code is not None else None
    stock_code = requested if requested in matrix.index else str(matrix.index[0])
    if requested is not None and requested not in matrix.index:
        print(f"stock_code={requested!r} not in bounded matrix; using {stock_code!r}")

    target = matrix.loc[[stock_code]]
    scores = cosine_similarity(target, matrix)[0]
    ranked = (
        pd.Series(scores, index=matrix.index, name="cosine_similarity")
        .drop(stock_code)
        .sort_values(ascending=False)
        .head(args.top_k)
    )

    descriptions = (
        clean[[col["stock"], col["description"]]]
        .dropna(subset=[col["description"]])
        .drop_duplicates(subset=[col["stock"]])
        .set_index(col["stock"])[col["description"]]
        .astype(str)
    )

    print(f"clean transactions={len(clean):,}")
    print(f"item-user matrix={matrix.shape}")
    print(f"target stock code={stock_code!r} | {descriptions.get(stock_code, '')}")
    print("nearest items:")
    for item, score in ranked.items():
        print(f"{item:>12}  {score:.3f}  {descriptions.get(item, '')}")


if __name__ == "__main__":
    main()
