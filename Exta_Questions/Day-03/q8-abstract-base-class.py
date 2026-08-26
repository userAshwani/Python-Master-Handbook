"""
Q8: class Shape(ABC) with abstract method area(); Circle and Square subclass
it and implement area(). Demonstrates abc.ABC + @abstractmethod.

Input:  Circle(2).area()
Output: ~12.566 (pi * r^2)
"""

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        # TODO
        pass


class Circle(Shape):
    def __init__(self, radius):
        # TODO
        pass

    def area(self):
        # TODO
        pass


class Square(Shape):
    def __init__(self, side):
        # TODO
        pass

    def area(self):
        # TODO
        pass


# --- TEST ---
# print(round(Circle(2).area(), 3))  # expected: 12.566
# print(Square(3).area())            # expected: 9
