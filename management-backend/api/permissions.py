from rest_framework import permissions

class IsAuthenticatedAndVerifiedPermission(permissions.BasePermission):
    """
    Global permission to only allow authenticated and verified users to access a view.
    """

    def has_permission(self, request, view):
        return not request.user.is_anonymous and request.user.is_verified