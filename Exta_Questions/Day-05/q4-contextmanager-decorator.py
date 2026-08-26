"""
Q4: temp_setting(config, key, value) — use @contextlib.contextmanager to
temporarily override config[key] for the duration of a `with` block, then
restore the original value on exit.

Input:  with temp_setting(cfg, "debug", True): ...
Output: cfg["debug"] is True inside the block, restored after
"""

from contextlib import contextmanager


@contextmanager
def temp_setting(config, key, value):
    # TODO
    pass


# --- TEST ---
# cfg = {"debug": False}
# with temp_setting(cfg, "debug", True):
#     print(cfg["debug"])  # expected: True
# print(cfg["debug"])      # expected: False
