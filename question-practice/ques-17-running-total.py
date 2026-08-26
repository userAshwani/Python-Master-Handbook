"""
QUESTION: running_total(records, key) / moving_average(records, key, n) —
compute a cumulative running sum and an n-window moving average over a list of
records' numeric field. Used by pro-4-analytics-engine for trend reporting.

Input:  running_total([{"qty": 10}, {"qty": 20}, {"qty": 5}], "qty")
Output: [10, 30, 35]
"""


def running_total(records, key):
    # TODO
    pass


def moving_average(records, key, n):
    # TODO
    pass


# --- TEST ---
# data = [{"qty": 10}, {"qty": 20}, {"qty": 5}, {"qty": 15}]
# print(running_total(data, "qty"))       # expected: [10, 30, 35, 50]
# print(moving_average(data, "qty", 2))   # expected: [10.0, 15.0, 12.5, 10.0]
