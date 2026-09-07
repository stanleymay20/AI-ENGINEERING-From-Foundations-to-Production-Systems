"""Chapters 3-4 reference: Online Retail II ingestion, quality checks, and EDA.

Run first:
    python companion/download_datasets.py --dataset online_retail_ii --include-large

The script reads the official UCI XLSX file from data/ and reports basic quality,
cancellation, revenue, and customer-level statistics without mutating the raw file.
"""
from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd


def find_workbook(data_root: Path) -> Path:
    root = data_root / "uci" / "online_retail_ii" / "raw"
    candidates = sorted(root.rglob("*.xlsx"))
    if not candidates:
        raise FileNotFoundError(
            "Online Retail II workbook not found. Run: "
            "python companion/download_datasets.py --dataset online_retail_ii --include-large"
        )
    return candidates[0]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-root", default="data")
    args = parser.parse_args()

    path = find_workbook(Path(args.data_root))
    print(f"Reading {path}")
    sheets = pd.read_excel(path, sheet_name=None)
    df = pd.concat(sheets.values(), ignore_index=True)

    df.columns = [str(c).strip() for c in df.columns]
    invoice_col = "InvoiceNo" if "InvoiceNo" in df.columns else "Invoice"
    customer_col = "CustomerID" if "CustomerID" in df.columns else "Customer ID"

    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"], errors="coerce")
    df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
    df["UnitPrice"] = pd.to_numeric(df["UnitPrice"], errors="coerce")
    df["Revenue"] = df["Quantity"] * df["UnitPrice"]
    cancelled = df[invoice_col].astype(str).str.upper().str.startswith("C")

    print(f"rows={len(df):,} columns={len(df.columns)}")
    print(f"date range={df['InvoiceDate'].min()} to {df['InvoiceDate'].max()}")
    print(f"cancelled rows={cancelled.sum():,} ({cancelled.mean():.2%})")
    print(f"missing customer ids={df[customer_col].isna().sum():,}")
    print(f"non-positive quantity rows={(df['Quantity'] <= 0).sum():,}")
    print(f"non-positive price rows={(df['UnitPrice'] <= 0).sum():,}")

    valid = df.loc[
        ~cancelled & (df["Quantity"] > 0) & (df["UnitPrice"] > 0)
    ].copy()
    customer_revenue = valid.groupby(customer_col, dropna=True)["Revenue"].sum()
    print(f"valid gross revenue={valid['Revenue'].sum():,.2f}")
    print(f"customers with valid purchases={customer_revenue.size:,}")
    print("top 5 customer revenue:")
    print(customer_revenue.sort_values(ascending=False).head(5).round(2).to_string())


if __name__ == "__main__":
    main()
