"""
Q2: run_producer_consumer(items) — use queue.Queue with a producer thread
that pushes items and a consumer thread that pops and processes them,
returning the list of processed results once the queue is drained.

Input:  run_producer_consumer([1, 2, 3])
Output: [2, 4, 6]  (each item doubled by the consumer)
"""

import threading
import queue


def run_producer_consumer(items):
    # TODO
    pass


# --- TEST ---
# print(run_producer_consumer([1, 2, 3]))  # expected: [2, 4, 6]
