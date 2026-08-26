"""
QUESTION: curry(fn) / partial_(fn, *args) — convert a multi-arg function into a
chain of single-arg calls, and a helper that pre-fills leading arguments.
Needed so pro-1-py-utils can build reusable, partially-applied pipeline steps.

Input:  curry(lambda a, b, c: a + b + c)(1)(2)(3)
Output: 6
"""


def curry(fn):
    # TODO
    pass


def partial_(fn, *preset_args):
    # TODO
    pass


# --- TEST ---
# add3 = lambda a, b, c: a + b + c
# print(curry(add3)(1)(2)(3))          # expected: 6
# add_five = partial_(add3, 2, 3)
# print(add_five(1))                   # expected: 6
