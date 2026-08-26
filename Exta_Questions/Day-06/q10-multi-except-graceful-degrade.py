"""
Q10: fetch_config_value(source, key) — try multiple lookup strategies in
order (dict lookup, then environment variable, then a hardcoded default),
using separate except clauses for KeyError and any other lookup failure.

Input:  fetch_config_value({}, "TIMEOUT")
Output: falls back through each strategy and returns a default like "30"
"""

import os


def fetch_config_value(source, key):
    # TODO
    pass


# --- TEST ---
# print(fetch_config_value({}, "TIMEOUT"))  # expected: some default value, e.g. '30'
