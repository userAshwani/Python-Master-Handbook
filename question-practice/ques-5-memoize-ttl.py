"""
QUESTION: memoize(fn, ttl=None) — decorator caching a function's return value per
argument set, with an optional time-to-live (seconds) after which entries expire.
Needed by pro-1-py-utils to avoid recomputing expensive lookups on hot paths.

Input:  @memoize(ttl=2) def slow(n): ...
Output: repeated calls with same args return cached result until ttl elapses
"""


def memoize(fn=None, ttl=None):
    # TODO
    pass


# --- TEST ---
# import time
# @memoize(ttl=1)
# def add(a, b):
#     print("computing...")
#     return a + b
# print(add(1, 2))  # prints "computing..." then 3
# print(add(1, 2))  # cached, no print, returns 3
# time.sleep(1.1)
# print(add(1, 2))  # ttl expired, prints "computing..." again
