"""
Q1: class ThreadSafeCounter() — a counter class using threading.Lock so
increment() is safe to call from multiple threads at once without losing
updates.

Input:  10 threads each call counter.increment() 1000 times
Output: counter.value == 10000 (no lost updates)
"""

import threading


class ThreadSafeCounter:
    def __init__(self):
        # TODO
        pass

    def increment(self):
        # TODO
        pass


# --- TEST ---
# counter = ThreadSafeCounter()
# threads = [threading.Thread(target=lambda: [counter.increment() for _ in range(1000)]) for _ in range(10)]
# [t.start() for t in threads]
# [t.join() for t in threads]
# print(counter.value)  # expected: 10000
