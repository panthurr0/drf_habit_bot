from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """Проверяет, является ли пользователь владельцем объекта."""

    message = "Доступно только владельцу"

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
