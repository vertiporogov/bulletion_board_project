from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'admin'


class IsOwner(BasePermission):
    message = "Вы не являетесь владельцем"

    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner:
            return True
        return False
