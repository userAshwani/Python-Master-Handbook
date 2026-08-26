"""
Q3: async def fetch_all(urls) — use asyncio.gather to run several mock
async fetch coroutines concurrently and return all their results in order.

Input:  await fetch_all(["/a", "/b", "/c"])
Output: ["data:/a", "data:/b", "data:/c"]
"""

import asyncio


async def fetch_one(url):
    await asyncio.sleep(0.05)
    return f"data:{url}"


async def fetch_all(urls):
    # TODO
    pass


# --- TEST ---
# print(asyncio.run(fetch_all(["/a", "/b", "/c"])))
# expected: ['data:/a', 'data:/b', 'data:/c']
