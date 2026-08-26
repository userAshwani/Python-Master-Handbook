"""
Q9: merge_unequal(list_a, list_b, fill="-") — use itertools.zip_longest to
pair up two lists of different lengths, filling missing values with `fill`.

Input:  merge_unequal([1, 2, 3], ["a", "b"])
Output: [(1, "a"), (2, "b"), (3, "-")]
"""

from itertools import zip_longest


def merge_unequal(list_a, list_b, fill="-"):
    # TODO
    pass


# --- TEST ---
# print(merge_unequal([1, 2, 3], ["a", "b"]))
# expected: [(1, 'a'), (2, 'b'), (3, '-')]
