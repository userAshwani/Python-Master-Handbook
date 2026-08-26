"""
QUESTION: class RateLimiter(capacity, refill_rate) — token-bucket rate limiter
with allow(key) returning True/False, refilling tokens over time. Used by
pro-4-analytics-engine to throttle expensive report generation per user/key.

Input:  limiter = RateLimiter(capacity=2, refill_rate=1); limiter.allow("user1")
Output: True, True, then False until a token refills
"""


class RateLimiter:
    def __init__(self, capacity, refill_rate):
        # TODO
        pass

    def allow(self, key):
        # TODO
        pass


# --- TEST ---
# limiter = RateLimiter(capacity=2, refill_rate=1)
# print(limiter.allow("user1"))  # expected: True
# print(limiter.allow("user1"))  # expected: True
# print(limiter.allow("user1"))  # expected: False (bucket empty)
