"""
Q10: safe_get(d, key_path, default=None) — safely fetch a value from a
nested dict using a dot-separated key path, returning `default` if any key
in the path is missing (without raising KeyError).

Input:  safe_get({"a": {"b": {"c": 5}}}, "a.b.c")
Output: 5
"""


def safe_get(d, key_path, default=None):
    # TODO
    pass


# --- TEST ---
# print(safe_get({"a": {"b": {"c": 5}}}, "a.b.c"))     # expected: 5
# print(safe_get({"a": {"b": {}}}, "a.b.c", "none"))   # expected: 'none'
