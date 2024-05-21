from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    "This will give access to authorize owners to make changes to an object"

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.user == request.user