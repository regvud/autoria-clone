from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user and request.user.is_staff and request.user.is_superuser
        )


class IsManager(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff)


class IsSeller(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user)


class IsPremium(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_premium)
