"""
Q8: read_json_safe(path, default=None) — read and parse a JSON file,
returning `default` instead of raising if the file is missing or contains
invalid JSON.

Input:  read_json_safe("missing.json", default={})
Output: {}
"""

import json


def read_json_safe(path, default=None):
    # TODO
    pass


# --- TEST ---
# print(read_json_safe("missing.json", default={}))  # expected: {}
