"""
QUESTION: safe_json_dumps(value) — serialize a value to a JSON string that
tolerates circular references (replacing repeated/self-referencing objects with
a marker instead of raising RecursionError). Used by the pro-final-pymart
capstone to safely log audit trails that may contain shared object references.

Input:  d = {}; d["self"] = d; safe_json_dumps(d)
Output: '{"self": "<circular>"}'
"""


def safe_json_dumps(value):
    # TODO
    pass


# --- TEST ---
# d = {"a": 1}
# d["self"] = d
# print(safe_json_dumps(d))  # expected: '{"a": 1, "self": "<circular>"}'
