"""
QUESTION: deep_diff(a, b) — recursively compare two nested dicts and return only
the keys whose values changed, each as {"from": old, "to": new}. Needed by
pro-2-data-normalizer / the capstone audit trail to log what changed between runs.

Input:  deep_diff({"status": "pending", "qty": 5}, {"status": "shipped", "qty": 5})
Output: {"status": {"from": "pending", "to": "shipped"}}
"""


def deep_diff(a, b):
    # TODO
    pass


# --- TEST ---
# before = {"status": "pending", "qty": 5}
# after = {"status": "shipped", "qty": 5}
# print(deep_diff(before, after))
# expected: {'status': {'from': 'pending', 'to': 'shipped'}}
