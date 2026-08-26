"""
QUESTION: multi_key_sort(records, config) — sort a list of dicts by multiple
keys in priority order, each with its own ascending/descending direction.
Used by pro-4-analytics-engine to build prioritized inventory reports.

Input:  multi_key_sort(records, [("warehouse", "asc"), ("quantity", "desc")])
Output: records sorted by warehouse ascending, then quantity descending
"""


def multi_key_sort(records, config):
    # TODO
    pass


# --- TEST ---
# data = [
#     {"warehouse": "WH-2", "quantity": 10},
#     {"warehouse": "WH-1", "quantity": 30},
#     {"warehouse": "WH-1", "quantity": 50},
# ]
# result = multi_key_sort(data, [("warehouse", "asc"), ("quantity", "desc")])
# print([r["quantity"] for r in result])  # expected: [50, 30, 10]
