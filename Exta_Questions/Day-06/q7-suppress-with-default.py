"""
Q7: default_on_error(default_value) — a decorator factory that catches any
exception the wrapped function raises and returns `default_value` instead,
rather than propagating the error.

Input:  @default_on_error(0) def parse_int(s): return int(s)
Output: parse_int("abc") -> 0   parse_int("5") -> 5
"""


def default_on_error(default_value):
    # TODO
    pass


# --- TEST ---
# @default_on_error(0)
# def parse_int(s):
#     return int(s)
# print(parse_int("5"))    # expected: 5
# print(parse_int("abc"))  # expected: 0
