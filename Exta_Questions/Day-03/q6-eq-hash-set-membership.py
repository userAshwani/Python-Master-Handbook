"""
Q6: class Point(x, y) — implement __eq__ and __hash__ so two Points with
equal coordinates are considered equal and can be stored/deduplicated in a set.

Input:  {Point(1, 2), Point(1, 2), Point(3, 4)}
Output: a set with 2 distinct Point elements
"""


class Point:
    def __init__(self, x, y):
        # TODO
        pass

    def __eq__(self, other):
        # TODO
        pass

    def __hash__(self):
        # TODO
        pass


# --- TEST ---
# pts = {Point(1, 2), Point(1, 2), Point(3, 4)}
# print(len(pts))  # expected: 2
