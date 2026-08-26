"""
Q10: class Version(major, minor) with @functools.total_ordering — implement
__eq__ and __lt__ only, and let total_ordering fill in <=, >, >= so Version
instances can be sorted.

Input:  sorted([Version(1, 5), Version(1, 2), Version(2, 0)])
Output: [Version(1,2), Version(1,5), Version(2,0)]
"""

from functools import total_ordering


@total_ordering
class Version:
    def __init__(self, major, minor):
        # TODO
        pass

    def __eq__(self, other):
        # TODO
        pass

    def __lt__(self, other):
        # TODO
        pass


# --- TEST ---
# versions = [Version(1, 5), Version(1, 2), Version(2, 0)]
# result = sorted(versions)
# print([(v.major, v.minor) for v in result])
# expected: [(1, 2), (1, 5), (2, 0)]
