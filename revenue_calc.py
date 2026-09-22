"""
Meridian Orders API assignment — revenue verification script.

Sums `total` across orders_page1.json and orders_page2.json.
Two corrections are applied and clearly flagged:

1. ord_1006's amounts are recorded as decimal dollars, not integer cents
   (every other order uses integer cents, e.g. 5470 == $54.70). Treated
   as a data-entry bug and read as $53.62, not divided by 100 again.
2. Refunded orders (status == "refunded") are excluded from revenue,
   since a refund reverses the sale. A second total that includes them
   is also printed for comparison.
"""

import json

def load(path):
    with open(path) as f:
        return json.load(f)["data"]

orders = load("orders_page1.json") + load("orders_page2.json")

DOLLAR_FORMAT_BUG_IDS = {"ord_1006"}  # already in dollars, not cents

net_revenue = 0.0
gross_revenue = 0.0
for o in orders:
    total = o["total"]
    dollars = total if o["id"] in DOLLAR_FORMAT_BUG_IDS else total / 100
    gross_revenue += dollars
    if o["status"] != "refunded":
        net_revenue += dollars

print(f"Gross revenue (all orders, refunds included): ${gross_revenue:,.2f}")
print(f"Net revenue (refunded orders excluded):        ${net_revenue:,.2f}")
