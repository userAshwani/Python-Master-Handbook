"""
QUESTION: pivot_table(records, row, col, val) — build a 2D aggregation table
summing `val` grouped by `row` then `col`. Used by pro-4-analytics-engine to
produce warehouse x status inventory breakdowns.

Input:  pivot_table(orders, "warehouse", "status", "quantity")
Output: {"WH-1": {"shipped": 120, "pending": 30}, "WH-2": {"shipped": 45}}
"""


def pivot_table(records, row, col, val):
    # TODO
    pass


# --- TEST ---
# orders = [
#     {"warehouse": "WH-1", "status": "shipped", "quantity": 120},
#     {"warehouse": "WH-1", "status": "pending", "quantity": 30},
#     {"warehouse": "WH-2", "status": "shipped", "quantity": 45},
# ]
# print(pivot_table(orders, "warehouse", "status", "quantity"))
# expected: {'WH-1': {'shipped': 120, 'pending': 30}, 'WH-2': {'shipped': 45}}
