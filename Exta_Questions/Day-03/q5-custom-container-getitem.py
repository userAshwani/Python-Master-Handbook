"""
Q5: class Row() — a custom container implementing __getitem__ and
__setitem__ backed by an internal dict, so instances support row["col"]
read/write syntax.

Input:  r = Row(); r["sku"] = "A1"; r["sku"]
Output: "A1"
"""


class Row:
    def __init__(self):
        # TODO
        pass

    def __getitem__(self, key):
        # TODO
        pass

    def __setitem__(self, key, value):
        # TODO
        pass


# --- TEST ---
# r = Row()
# r["sku"] = "A1"
# print(r["sku"])  # expected: 'A1'
