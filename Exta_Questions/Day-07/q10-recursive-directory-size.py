"""
Q10: directory_size(node) — recursively compute the total size of a mock
nested directory tree, where each dict node has "files" (a list of byte
sizes) and "folders" (a dict of subfolder name -> nested node).

Input:  {"files": [10, 20], "folders": {"sub": {"files": [5], "folders": {}}}}
Output: 35
"""


def directory_size(node):
    # TODO
    pass


# --- TEST ---
# tree = {"files": [10, 20], "folders": {"sub": {"files": [5], "folders": {}}}}
# print(directory_size(tree))  # expected: 35
