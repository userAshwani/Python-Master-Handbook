"""
Q9: class TempFile(path, content) — a context manager that writes `content`
to `path` on entry and always deletes the file on exit, even if an
exception occurs inside the `with` block.

Input:  with TempFile("scratch.txt", "data") as p: ...
Output: scratch.txt exists during the block, is deleted after
"""

import os


class TempFile:
    def __init__(self, path, content):
        # TODO
        pass

    def __enter__(self):
        # TODO
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        # TODO
        pass


# --- TEST ---
# with TempFile("scratch.txt", "data") as p:
#     print(os.path.exists(p))  # expected: True
# print(os.path.exists("scratch.txt"))  # expected: False
