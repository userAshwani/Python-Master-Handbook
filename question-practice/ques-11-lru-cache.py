"""
QUESTION: class LRUCache(capacity) — an OrderedDict-based cache that evicts the
least-recently-used entry once it exceeds capacity. Used by pro-3-rbac-engine to
cache resolved permission sets per role without unbounded memory growth.

Input:  cache = LRUCache(2); cache.put("a", 1); cache.put("b", 2); cache.put("c", 3)
Output: cache.get("a") -> -1 (evicted)   cache.get("c") -> 3
"""

from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity):
        # TODO
        pass

    def get(self, key):
        # TODO
        pass

    def put(self, key, value):
        # TODO
        pass


# --- TEST ---
# cache = LRUCache(2)
# cache.put("a", 1)
# cache.put("b", 2)
# cache.put("c", 3)
# print(cache.get("a"))  # expected: -1
# print(cache.get("c"))  # expected: 3
