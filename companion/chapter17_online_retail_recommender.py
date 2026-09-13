"""Chapter 17 reference: item-item recommendation with Online Retail II.

The book reuses the controlled UCI Online Retail II source from Chapters 3-4.
Prepare it with:
    python companion/download_datasets.py --dataset online_retail_ii --include-large

The lab treats valid customer-product purchases as implicit feedback. It does not
invent explicit ratings from transaction quantities.
"""
from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.sparse import csr_matrix
from sklearn.metrics.pairwise import cosine_similarity


def find_workbook(data_root: Path) -> Path:
    root = data_root / "uci" / "online_retail_ii" / "raw"
    matches = sorted(root.rglob("*.xlsx")) + sorted(root.rglob("*.xls"))
    if not matches:
        raise FileNotFoundError(
            "Online Retail II workbook not found. Run the controlled downloader with "
            "--dataset online_retail_ii --include-large."
        )
    return matches[0]


def load_transactions(path: Path) -> pd.DataFrame:
    sheets = pd.read_excel(path, sheet_name=None)
    frame = pd.concat(sheets.values(), ignore_index=True)

    aliases = {
        "InvoiceNo": "Invoice",
        "UnitPrice": "Price",
        "CustomerID": "Customer ID",
    }
    frame = frame.rename(columns={k: v for k, v in aliases.items() if k in frame.columns})
    required = {"Invoice", "StockCode", "Quantity", "Customer ID"}
    missing = required - set(frame.columns)
    if missing:
        raise ValueError(f"Online Retail II workbook is missing columns: {sorted(missing)}")

    frame = frame.dropna(subset=["Customer ID", "StockCode", "Invoice"])
    frame["Invoice"] = frame["Invoice"].astype(str)
    frame["StockCode"] = frame["StockCode"].astype(str)
    frame["Customer ID"] = frame["Customer ID"].astype(str).str.replace(r"\.0$", "", regex=True)
    frame["Quantity"] = pd.to_numeric(frame["Quantity"], errors="coerce")

    # C-prefixed invoices are cancellations/returns in this dataset. The core
    # recommendation interaction matrix uses positive completed-purchase evidence.
    frame = frame[(~frame["Invoice"].str.upper().str.startswith("C")) & (frame["Quantity"] > 0)]
    return frame


def build_binary_interactions(
    frame: pd.DataFrame,
    min_item_customers: int,
    min_customer_items: int,
) -> tuple[csr_matrix, np.ndarray, np.ndarray]:
    pairs = frame[["Customer ID", "StockCode"]].drop_duplicates()

    item_counts = pairs.groupby("StockCode")["Customer ID"].nunique()
    keep_items = item_counts[item_counts >= min_item_customers].index
    pairs = pairs[pairs["StockCode"].isin(keep_items)]

    customer_counts = pairs.groupby("Customer ID")["StockCode"].nunique()
    keep_customers = customer_counts[customer_counts >= min_customer_items].index
    pairs = pairs[pairs["Customer ID"].isin(keep_customers)]

    customers = pd.Index(sorted(pairs["Customer ID"].unique()))
    items = pd.Index(sorted(pairs["StockCode"].unique()))
    customer_codes = customers.get_indexer(pairs["Customer ID"])
    item_codes = items.get_indexer(pairs["StockCode"])

    matrix = csr_matrix(
        (np.ones(len(pairs), dtype=np.float32), (customer_codes, item_codes)),
        shape=(len(customers), len(items)),
    )
    return matrix, customers.to_numpy(), items.to_numpy()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-root", default="data")
    parser.add_argument("--stock-code", default=None)
    parser.add_argument("--min-item-customers", type=int, default=20)
    parser.add_argument("--min-customer-items", type=int, default=5)
    parser.add_argument("--top-n", type=int, default=10)
    args = parser.parse_args()

    workbook = find_workbook(Path(args.data_root))
    transactions = load_transactions(workbook)
    matrix, customers, items = build_binary_interactions(
        transactions,
        min_item_customers=args.min_item_customers,
        min_customer_items=args.min_customer_items,
    )
    if matrix.shape[0] == 0 or matrix.shape[1] == 0:
        raise RuntimeError("No interactions remain after the configured support filters.")

    item_user = matrix.T.tocsr()
    popularity = np.asarray(item_user.sum(axis=1)).ravel()

    if args.stock_code is None:
        target_idx = int(popularity.argmax())
        stock_code = str(items[target_idx])
    else:
        matches = np.flatnonzero(items == args.stock_code)
        if not len(matches):
            raise ValueError(
                f"stock_code={args.stock_code!r} is absent after support filtering; "
                "choose another code or lower the thresholds."
            )
        target_idx = int(matches[0])
        stock_code = args.stock_code

    scores = cosine_similarity(item_user[target_idx], item_user).ravel()
    order = np.argsort(-scores)
    order = order[order != target_idx][: args.top_n]

    print(f"source={workbook}")
    print(f"customers={len(customers)} items={len(items)} interactions={matrix.nnz}")
    print(f"nearest items to stock_code={stock_code}:")
    for idx in order:
        print(
            f"{items[idx]}\tcosine={scores[idx]:.3f}\t"
            f"customer_support={int(popularity[idx])}"
        )


if __name__ == "__main__":
    main()
