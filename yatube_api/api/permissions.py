from rest_framework import permissions


class AuthorOrReadOnly(permissions.BasePermission):
    """Checks whether the user is the author of the object
    to give him permission to change the object.
    """
    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return view.action == 'retrieve' or obj.author == request.user
