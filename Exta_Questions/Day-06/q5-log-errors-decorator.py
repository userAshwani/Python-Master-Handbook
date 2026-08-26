"""
Q5: log_errors(fn) — a decorator that catches any exception raised by the
wrapped function, prints "ERROR in <fn name>: <message>", and then
re-raises the exception so callers still see it.

Input:  @log_errors def risky(): raise ValueError("bad")
Output: prints "ERROR in risky: bad" then re-raises ValueError
"""


def log_errors(fn):
    # TODO
    pass


# --- TEST ---
# @log_errors
# def risky():
#     raise ValueError("bad")
# risky()  # expected: prints 'ERROR in risky: bad' then raises ValueError
