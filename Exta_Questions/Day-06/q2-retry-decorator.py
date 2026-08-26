"""
Q2: retry(max_attempts) — a decorator factory that retries a function up to
`max_attempts` times if it raises an exception, re-raising the last
exception if all attempts fail.

Input:  @retry(max_attempts=3) def flaky(): ...
Output: function is called again on failure, up to 3 total attempts
"""


def retry(max_attempts=3):
    # TODO
    pass


# --- TEST ---
# attempts = {"count": 0}
# @retry(max_attempts=3)
# def flaky():
#     attempts["count"] += 1
#     if attempts["count"] < 3:
#         raise ValueError("fail")
#     return "ok"
# print(flaky())            # expected: 'ok'
# print(attempts["count"])  # expected: 3
