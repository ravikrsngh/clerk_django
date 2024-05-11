from rest_framework.permissions import BasePermission

class ClerkAuthenticated(BasePermission):
    """
    Allows access only to authenticated users.
    """

    def has_permission(self, request, view):
        return request.clerk_user.get('is_authenticated',False)