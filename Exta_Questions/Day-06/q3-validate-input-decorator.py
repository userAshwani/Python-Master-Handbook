"""
Q3: validate_positive(fn) — a decorator that inspects a wrapped function's
first argument and raises ValueError before calling it if that argument is
negative.

Input:  @validate_positive def square(n): return n * n
Output: square(-3) raises ValueError; square(3) returns 9
"""


def validate_positive(fn):
    # TODO
    pass


# --- TEST ---
# @validate_positive
# def square(n):
#     return n * n
# print(square(3))   # expected: 9
# square(-3)          # expected: raises ValueError
