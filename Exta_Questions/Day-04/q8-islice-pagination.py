"""
Q8: paginate(iterable, page, page_size) — use itertools.islice to return
just one "page" of items from a (possibly large/lazy) iterable without
materializing the whole thing first.

Input:  paginate(range(100), page=2, page_size=10)
Output: [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
"""

from itertools import islice


def paginate(iterable, page, page_size):
    # TODO
    pass


# --- TEST ---
# print(paginate(range(100), page=2, page_size=10))
# expected: [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
