"""
pro-3-rbac-engine — rbac.py
Role-based access control: caching, SKU search, and field masking.
See about.txt for full requirements.
"""

from collections import OrderedDict


# --- 1. LRU CACHE ---
class LRUCache:
    def __init__(self, capacity):
        # TODO (see ques-11-lru-cache.py)
        pass

    def get(self, key):
        # TODO
        pass

    def put(self, key, value):
        # TODO
        pass


# --- 2. TRIE ---
class Trie:
    def __init__(self):
        # TODO (see ques-12-trie.py)
        pass

    def insert(self, word):
        # TODO
        pass

    def starts_with(self, prefix):
        # TODO
        pass


# --- 3. FIELD MASKING ---
def mask_email(email):
    # TODO (see ques-13-field-masking.py)
    pass


def mask_phone(phone):
    # TODO (see ques-13-field-masking.py)
    pass


# --- 4. APPLY RBAC ---
def apply_rbac(record, role):
    # TODO: use resolve_permissions() + mask_email()/mask_phone()
    pass
