"""
Q9: class ManagedResource(name) — a context manager class implementing
__enter__ and __exit__ that prints when the resource opens and closes,
usable with `with ManagedResource("db") as r:`.

Input:  with ManagedResource("db") as r: ...
Output: prints "opening db" then block runs then prints "closing db"
"""


class ManagedResource:
    def __init__(self, name):
        # TODO
        pass

    def __enter__(self):
        # TODO
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        # TODO
        pass


# --- TEST ---
# with ManagedResource("db") as r:
#     print("using", r)
# expected prints: 'opening db', 'using db', 'closing db'
