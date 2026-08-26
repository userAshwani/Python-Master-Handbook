"""
QUESTION: mask_email(email) / mask_phone(phone) — partially mask sensitive contact
fields, keeping just enough visible for identification. Used by pro-3-rbac-engine
to protect PII from roles that shouldn't see it in full.

Input:  mask_email("jane.doe@pymart.io")   mask_phone("9876543210")
Output: "ja***@pymart.io"                  "98******10"
"""


def mask_email(email):
    # TODO
    pass


def mask_phone(phone):
    # TODO
    pass


# --- TEST ---
# print(mask_email("jane.doe@pymart.io"))  # expected: 'ja***@pymart.io'
# print(mask_phone("9876543210"))          # expected: '98******10'
