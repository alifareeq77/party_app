from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    safe_methods are ('GET','HEAD','OPTIONS')
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            # if request is get we treat the request as it is from the owner
            return True

        # Write permissions are only allowed to the owner of the party.
        # if request is not from the user and the method isn't safe then we'll return auth error
        return obj.creator == request.user  # return false for not owner so 403
