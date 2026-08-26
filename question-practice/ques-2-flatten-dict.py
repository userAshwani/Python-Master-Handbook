"""
QUESTION: flatten_dict(d, prefix="") — flatten a nested dict into dot-notation keys
Needed so pro-1-py-utils can turn nested inventory records into flat, loggable rows.

Input:  {"a": {"b": 1, "c": {"d": 2}}}
Output: {"a.b": 1, "a.c.d": 2}
"""


def flatten_dict(d, prefix=""):
    # TODO
    pass


# --- TEST ---
# print(flatten_dict({"a": {"b": 1, "c": {"d": 2}}}))
# expected: {'a.b': 1, 'a.c.d': 2}
