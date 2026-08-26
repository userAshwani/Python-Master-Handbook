"""
Q6: append_log_entry(path, message) — append a timestamped message as a new
line to a log file, opening in append mode and always closing the file
(via `with`) even if writing fails.

Input:  append_log_entry("app.log", "server started")
Output: a new line like "2026-08-26T00:00:00 server started" appended
"""

from datetime import datetime


def append_log_entry(path, message):
    # TODO
    pass


# --- TEST ---
# append_log_entry("app.log", "server started")
# then read app.log: expected last line ends with 'server started'
