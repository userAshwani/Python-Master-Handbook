"""
Q7: class Product(price) — use @property and a setter that raises
ValueError if a negative price is assigned, keeping the internal value
always valid.

Input:  p = Product(10); p.price = -5
Output: raises ValueError
"""


class Product:
    def __init__(self, price):
        # TODO
        pass

    @property
    def price(self):
        # TODO
        pass

    @price.setter
    def price(self, value):
        # TODO
        pass


# --- TEST ---
# p = Product(10)
# print(p.price)   # expected: 10
# p.price = -5      # expected: raises ValueError
