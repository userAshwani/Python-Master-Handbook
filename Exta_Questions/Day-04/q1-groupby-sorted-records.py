"""
Q1: group_records_by_category(records) — use itertools.groupby to group a
list of dicts by "category" (list must be sorted by that key first).

Input:  [{"category": "a", "v": 1}, {"category": "a", "v": 2}, {"category": "b", "v": 3}]
Output: {"a": [1, 2], "b": [3]}
"""

from itertools import groupby


def group_records_by_category(records):
    # TODO
    pass


# --- TEST ---
# data = [{"category": "a", "v": 1}, {"category": "a", "v": 2}, {"category": "b", "v": 3}]
# print(group_records_by_category(data))  # expected: {'a': [1, 2], 'b': [3]}
