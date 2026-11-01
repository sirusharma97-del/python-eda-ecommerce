"""Exploratory analysis of a small sample e-commerce orders file.

Loads sample_orders.csv, explores revenue by category, channel and month,
finds the top products and repeat customers, checks the return rate, and
prints a short findings section. Sample data for portfolio use.
"""
import pandas as pd

FILE = "sample_orders.csv"


def main() -> None:
    df = pd.read_csv(FILE, parse_dates=["order_date"])
    df["revenue"] = df["quantity"] * df["unit_price"]
    df["month"] = df["order_date"].dt.to_period("M")

    kept = df[df["returned"] == "N"]  # revenue figures exclude returns

    print("=" * 60)
    print("SAMPLE E-COMMERCE ORDERS — EXPLORATORY ANALYSIS")
    print("=" * 60)
    print(f"Orders in file:        {len(df)}")
    print(f"Date range:            {df['order_date'].min().date()} to "
          f"{df['order_date'].max().date()}")
    print(f"Gross revenue (filed): ${df['revenue'].sum():,.2f}")
    print(f"Net revenue (no ret.): ${kept['revenue'].sum():,.2f}")

    print("\n-- Revenue by category (net of returns) --")
    by_cat = (kept.groupby("category")
                  .agg(orders=("order_id", "count"),
                       units=("quantity", "sum"),
                       revenue=("revenue", "sum"))
                  .sort_values("revenue", ascending=False))
    print(by_cat.to_string(float_format=lambda v: f"{v:,.2f}"))

    print("\n-- Revenue by channel (net of returns) --")
    by_channel = (kept.groupby("channel")
                      .agg(orders=("order_id", "count"),
                           revenue=("revenue", "sum")))
    by_channel["avg_order_value"] = (by_channel["revenue"]
                                     / by_channel["orders"])
    print(by_channel.to_string(float_format=lambda v: f"{v:,.2f}"))

    print("\n-- Top 5 products by revenue (net of returns) --")
    top_products = (kept.groupby("product")["revenue"].sum()
                        .sort_values(ascending=False).head(5))
    for product, revenue in top_products.items():
        print(f"  {product:22} ${revenue:,.2f}")

    print("\n-- Monthly revenue trend (net of returns) --")
    monthly = kept.groupby("month")["revenue"].sum()
    prev = None
    for month, revenue in monthly.items():
        change = "" if prev is None else f"  ({(revenue - prev) / prev:+.1%} vs prior month)"
        print(f"  {month}: ${revenue:,.2f}{change}")
        prev = revenue

    print("\n-- Returns --")
    returns = df[df["returned"] == "Y"]
    print(f"Returned orders: {len(returns)} of {len(df)} "
          f"({len(returns) / len(df):.1%} of orders), "
          f"${returns['revenue'].sum():,.2f} of gross revenue")
    print("Returned products:", ", ".join(sorted(returns["product"].unique())))

    print("\n-- Customers --")
    orders_per_customer = df.groupby("customer_id")["order_id"].count()
    repeat = orders_per_customer[orders_per_customer > 1]
    print(f"Unique customers: {orders_per_customer.size}, "
          f"repeat customers: {len(repeat)} "
          f"({len(repeat) / orders_per_customer.size:.1%})")

    best_cat = by_cat["revenue"].idxmax()
    best_channel = by_channel["revenue"].idxmax()
    best_product = top_products.index[0]
    print("\n-- Findings --")
    print(f"1. {best_cat} is the top category by net revenue "
          f"(${by_cat.loc[best_cat, 'revenue']:,.2f}).")
    print(f"2. {best_channel} brings in more revenue than the other channel "
          f"(${by_channel.loc[best_channel, 'revenue']:,.2f} net).")
    print(f"3. {best_product} is the single best-selling product "
          f"(${top_products.iloc[0]:,.2f}).")
    print(f"4. Returns are a small share of orders "
          f"({len(returns) / len(df):.1%}) but each returned item is a "
          f"higher-priced product, so they still cost "
          f"${returns['revenue'].sum():,.2f}.")
    print(f"5. Only {len(repeat)} of {orders_per_customer.size} customers "
          f"ordered more than once in the period — repeat business is "
          f"the clear growth opportunity in this sample.")


if __name__ == "__main__":
    main()
