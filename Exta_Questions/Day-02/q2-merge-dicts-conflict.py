"""
Q2: merge_dicts_conflict(a, b, resolver) — merge two dicts; when a key
exists in both, call resolver(key, val_a, val_b) to decide the final value.

Input:  merge_dicts_conflict({"x": 1}, {"x": 5}, lambda k, a, b: a + b)
Output: {"x": 6}
"""


def merge_dicts_conflict(a, b, resolver):
    # TODO
    pass


# --- TEST ---
# print(merge_dicts_conflict({"x": 1}, {"x": 5}, lambda k, a, b: a + b))
# expected: {'x': 6}
