"""
Q6: fib(n) — apply the @functools.lru_cache decorator to a recursive
Fibonacci function so repeated calls reuse cached results instead of
recomputing the full recursion tree.

Input:  fib(10)
Output: 55
"""

from functools import lru_cache


@lru_cache(maxsize=None)
def fib(n):
    # TODO
    pass


# --- TEST ---
# print(fib(10))  # expected: 55
