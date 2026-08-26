"""
Q2: chain_all(*iterables) — use itertools.chain to lazily concatenate
multiple iterables into one flat iterator.

Input:  list(chain_all([1, 2], (3, 4), [5]))
Output: [1, 2, 3, 4, 5]
"""

from itertools import chain


def chain_all(*iterables):
    # TODO
    pass


# --- TEST ---
# print(list(chain_all([1, 2], (3, 4), [5])))  # expected: [1, 2, 3, 4, 5]
