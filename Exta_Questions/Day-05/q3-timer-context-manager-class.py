"""
Q3: class Timer() — a class-based context manager that records how long the
`with` block took to run, exposing it as self.elapsed after exit.

Input:  with Timer() as t: ...slow work...
Output: t.elapsed -> float seconds elapsed
"""

import time


class Timer:
    def __enter__(self):
        # TODO
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        # TODO
        pass


# --- TEST ---
# with Timer() as t:
#     time.sleep(0.1)
# print(t.elapsed >= 0.1)  # expected: True
