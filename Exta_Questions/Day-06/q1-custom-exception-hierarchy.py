"""
Q1: class InventoryError(Exception) / OutOfStockError(InventoryError) —
build a small custom exception hierarchy so callers can catch either the
specific error or any InventoryError broadly.

Input:  raise OutOfStockError("SKU A1 is out of stock")
Output: caught by `except InventoryError` as well as `except OutOfStockError`
"""


class InventoryError(Exception):
    pass


class OutOfStockError(InventoryError):
    # TODO: add any extra attributes/behavior needed
    pass


# --- TEST ---
# try:
#     raise OutOfStockError("SKU A1 is out of stock")
# except InventoryError as e:
#     print(str(e))  # expected: 'SKU A1 is out of stock'
