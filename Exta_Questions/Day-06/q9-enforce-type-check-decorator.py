"""
Q9: enforce_types(*expected_types) — a decorator factory that checks each
positional argument against the corresponding type in `expected_types`,
raising TypeError if any argument doesn't match before calling the function.

Input:  @enforce_types(int, int) def add(a, b): return a + b
Output: add(1, 2) -> 3   add("1", 2) -> raises TypeError
"""


def enforce_types(*expected_types):
    # TODO
    pass


# --- TEST ---
# @enforce_types(int, int)
# def add(a, b):
#     return a + b
# print(add(1, 2))   # expected: 3
# add("1", 2)          # expected: raises TypeError
