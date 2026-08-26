"""
Q7: parallel_map(fn, items, max_workers=4) — use
concurrent.futures.ThreadPoolExecutor to apply `fn` to every item in
parallel, returning results in the original input order.

Input:  parallel_map(lambda x: x * x, [1, 2, 3, 4])
Output: [1, 4, 9, 16]
"""

from concurrent.futures import ThreadPoolExecutor


def parallel_map(fn, items, max_workers=4):
    # TODO
    pass


# --- TEST ---
# print(parallel_map(lambda x: x * x, [1, 2, 3, 4]))  # expected: [1, 4, 9, 16]
