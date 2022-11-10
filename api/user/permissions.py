from rest_framework import permissions


class LoginCheckPermission(permissions.BasePermission):
    def has_permission(self, id, request, view):
        if id == self.request.user.id:
            return True
        return False
