"""
QUESTION: class Trie() — a prefix tree supporting insert(word) and
starts_with(prefix) for fast SKU autocomplete. Used by pro-3-rbac-engine to power
inventory search-as-you-type without scanning every SKU.

Input:  trie.insert("SKU-1001"); trie.insert("SKU-1002")
Output: trie.starts_with("SKU-10") -> True
"""


class Trie:
    def __init__(self):
        # TODO
        pass

    def insert(self, word):
        # TODO
        pass

    def starts_with(self, prefix):
        # TODO
        pass


# --- TEST ---
# trie = Trie()
# trie.insert("SKU-1001")
# trie.insert("SKU-1002")
# print(trie.starts_with("SKU-10"))  # expected: True
# print(trie.starts_with("SKU-99"))  # expected: False
