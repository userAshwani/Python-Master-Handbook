"""
Q10: make_greeter(greeting) — use functools.partial to pre-fill the
`greeting` argument of a generic greet(greeting, name) function, returning a
ready-to-use single-argument greeter.

Input:  make_greeter("Hello")("Sam")
Output: "Hello, Sam!"
"""

from functools import partial


def greet(greeting, name):
    return f"{greeting}, {name}!"


def make_greeter(greeting):
    # TODO
    pass


# --- TEST ---
# hello = make_greeter("Hello")
# print(hello("Sam"))  # expected: 'Hello, Sam!'
