"""
Q8: load_config(path) — attempt to open/parse a config file; if that fails,
raise a higher-level ConfigLoadError using `raise ... from e` so the
original exception is preserved as the cause (exception chaining).

Input:  load_config("missing.cfg")
Output: raises ConfigLoadError with __cause__ set to the original OSError
"""


class ConfigLoadError(Exception):
    pass


def load_config(path):
    # TODO
    pass


# --- TEST ---
# try:
#     load_config("missing.cfg")
# except ConfigLoadError as e:
#     print(type(e.__cause__))  # expected: <class 'FileNotFoundError'> (or OSError)
