# Python EDA — Sample E-Commerce Orders

An exploratory data analysis in Python (pandas) over a small sample of
e-commerce orders: load the file, look at it from several angles, and end
with plain-language findings instead of just tables.

All data is sample/practice data created for portfolio purposes. No real
company or customer data is used anywhere in this project.

## The question it answers

What does this order history actually say — which categories, channels,
and products drive revenue, how are sales trending month to month, and
where is the obvious opportunity?

## What was done

- Loaded `sample_orders.csv` (26 orders, Jan–Mar 2026) with pandas and
  added a calculated `revenue` column (quantity × unit price) and a
  `month` period column.
- Separated returned orders so revenue figures are reported **net of
  returns**, with returns analyzed on their own.
- Used `groupby` aggregations for revenue by category, by channel
  (including average order value), by product, and by month with a
  month-over-month percentage change.
- Counted orders per customer to measure repeat business.
- Printed a findings section written from the computed numbers, not
  typed-in conclusions.

## Findings (from running `analysis.py` on the sample data)

1. **Electronics leads** with $913.79 of $2,131.57 net revenue, ahead of
   Home ($651.78) and Clothing ($566.00).
2. **Online outsells Store** in total revenue ($1,138.80 vs. $992.77), but
   Store has the higher average order value ($99.28 vs. $81.34).
3. **Wireless Headphones** is the top product at $479.94 — more than a
   fifth of net revenue on its own.
4. Monthly revenue dipped in February (−8.2%) and recovered in March
   (+12.8%).
5. Returns are only 2 of 26 orders (7.7%), but both were higher-priced
   items (Coffee Maker, Winter Jacket) totaling $208.95.
6. Only 3 of 22 customers ordered more than once — repeat business is the
   clearest growth opportunity in this sample.

## Skills shown

- pandas: `groupby` aggregation, period conversion, sorting, calculated
  columns
- Separating gross vs. net figures and stating which one is being used
- Turning grouped output into short, honest findings

## Run it

```bash
pip install pandas
python analysis.py
```

## Files

- `README.md` — this file
- `analysis.py` — the exploratory analysis script
- `sample_orders.csv` — 26-row sample orders file the script reads
