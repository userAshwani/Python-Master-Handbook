"""
QUESTION: pipe(*fns) / compose(*fns) — build left-to-right and right-to-left
function composition decorators/helpers. Needed so pro-1-py-utils can chain
transform steps without deeply nested calls.

Input:  pipe(lambda x: x + 1, lambda x: x * 2)(3)
Output: 8   (compose would give 7, applying right-to-left)
"""


def pipe(*fns):
    # TODO
    pass


def compose(*fns):
    # TODO
    pass


# --- TEST ---
# print(pipe(lambda x: x + 1, lambda x: x * 2)(3))     # expected: 8
# print(compose(lambda x: x + 1, lambda x: x * 2)(3))  # expected: 7
