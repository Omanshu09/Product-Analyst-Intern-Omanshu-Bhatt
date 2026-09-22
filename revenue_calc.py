import json

def load(path):
    with open(path) as f:
        return json.load(f)["data"]

orders = load("orders_page1.json") + load("orders_page2.json")

DOLLAR_FORMAT_BUG_IDS = {"ord_1006"}  
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
