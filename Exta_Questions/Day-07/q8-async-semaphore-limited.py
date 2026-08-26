"""
Q8: async def run_limited(tasks, limit) — use asyncio.Semaphore to run a
list of async task callables with no more than `limit` running
concurrently, returning all results.

Input:  await run_limited([task1, task2, task3, task4], limit=2)
Output: [result1, result2, result3, result4], never more than 2 in flight
"""

import asyncio


async def run_limited(tasks, limit):
    # TODO
    pass


# --- TEST ---
# async def make_task(n):
#     async def t():
#         await asyncio.sleep(0.05)
#         return n
#     return t
# tasks = [asyncio.run(make_task(i)) for i in range(4)]
# print(asyncio.run(run_limited(tasks, limit=2)))  # expected: [0, 1, 2, 3]
