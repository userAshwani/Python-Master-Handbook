"""
QUESTION: resolve_permissions(tree, role) — recursively walk a nested role-
inheritance tree and return the flattened set of permissions granted to a role
(including permissions inherited from parent roles). Used by pro-3-rbac-engine.

Input:  tree with "admin" inheriting "editor" inheriting "viewer"
Output: resolve_permissions(tree, "admin") -> union of all 3 roles' permissions
"""


def resolve_permissions(tree, role):
    # TODO
    pass


# --- TEST ---
# tree = {
#     "viewer": {"perms": ["read"], "inherits": []},
#     "editor": {"perms": ["write"], "inherits": ["viewer"]},
#     "admin": {"perms": ["delete"], "inherits": ["editor"]},
# }
# print(sorted(resolve_permissions(tree, "admin")))
# expected: ['delete', 'read', 'write']
