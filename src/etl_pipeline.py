import pandas as pd
from pathlib import Path

RAW_FILE = Path("data/retail_sales_raw.csv")
CLEAN_FILE = Path("data/clean_sales.csv")
KPI_FILE = Path("data/monthly_kpi_summary.csv")

def load_data(path):
    """Read the raw CSV into a pandas DataFrame."""
    return pd.read_csv(path)

def clean_data(df):
    """Remove duplicates, handle missing values and add columns."""
    df = df.drop_duplicates()
    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
    df["region"] = df["region"].fillna("Unknown")
    df["discount"] = df["discount"].fillna(0)
    df = df[df["sales_amount"] >= 0]
    df = df[df["quantity"] > 0]
    df["order_year"] = df["order_date"].dt.year
    df["order_month"] = df["order_date"].dt.to_period("M").astype(str)
    df["profit_margin"] = (df["profit_amount"] / df["sales_amount"]).round(4)
    return df

def create_kpi_summary(df):
    """Calculate monthly KPIs by region and product category."""
    summary = df.groupby(
        ["order_month", "region", "product_category"], as_index=False
    ).agg(
        total_sales=("sales_amount", "sum"),
        total_profit=("profit_amount", "sum"),
        total_orders=("order_id", "nunique"),
        total_quantity=("quantity", "sum")
    )
    summary["profit_margin"] = (
        summary["total_profit"] / summary["total_sales"]
    ).round(4)
    return summary

def main():
    raw_df = load_data(RAW_FILE)
    clean_df = clean_data(raw_df)
    CLEAN_FILE.parent.mkdir(parents=True, exist_ok=True)
    clean_df.to_csv(CLEAN_FILE, index=False)
    kpi_df = create_kpi_summary(clean_df)
    kpi_df.to_csv(KPI_FILE, index=False)
    print("ETL completed successfully.")
    print(f"Rows after cleaning: {len(clean_df)}")
    print(f"Total sales: ${clean_df['sales_amount'].sum():,.2f}")
    print(f"Total profit: ${clean_df['profit_amount'].sum():,.2f}")

if __name__ == "__main__":
    main()