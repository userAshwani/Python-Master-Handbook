"""
QUESTION: fetch_batch_limited(fetch_fns, limit) — run a list of zero-arg callables
concurrently but never more than `limit` at once (ThreadPoolExecutor or an
asyncio.Semaphore), returning results in the original order. Used by
pro-2-data-normalizer to fetch multiple supplier feeds without overwhelming them.

Input:  fetch_batch_limited([fn1, fn2, fn3, fn4], limit=2)
Output: [fn1(), fn2(), fn3(), fn4()]  (never more than 2 running at once)
"""


def fetch_batch_limited(fetch_fns, limit):
    # TODO
    pass


# --- TEST ---
# import time
# def make_fn(n):
#     def fn():
#         time.sleep(0.1)
#         return n
#     return fn
# fns = [make_fn(i) for i in range(5)]
# print(fetch_batch_limited(fns, limit=2))  # expected: [0, 1, 2, 3, 4]
