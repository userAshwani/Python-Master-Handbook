"""
QUESTION: deep_copy(value) — recursively deep-copy any nested dict/list/tuple
Needed so pro-1-py-utils can hand out data without callers mutating shared state.

Input:  {"a": [1, {"b": 2}]}
Output: a fully independent copy (mutating the copy never touches the original)
"""


def deep_copy(value):
    # TODO
    pass


# --- TEST ---
# original = {"a": [1, {"b": 2}]}
# copy = deep_copy(original)
# copy["a"][1]["b"] = 999
# print(original)  # expected: {'a': [1, {'b': 2}]} (unchanged)
