"""
Q6: class ValidationError(Exception) — a custom exception that stores which
field failed and why, accessible as e.field and e.reason after being caught.

Input:  raise ValidationError(field="email", reason="missing @")
Output: e.field == "email", e.reason == "missing @"
"""


class ValidationError(Exception):
    def __init__(self, field, reason):
        # TODO
        pass


# --- TEST ---
# try:
#     raise ValidationError(field="email", reason="missing @")
# except ValidationError as e:
#     print(e.field, e.reason)  # expected: 'email missing @'
