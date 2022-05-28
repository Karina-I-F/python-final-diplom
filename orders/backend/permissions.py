from rest_framework import permissions


class DenyAny(permissions.BasePermission):
    def has_permission(self, request, view):
        self.message = 'Метод не доступен'
        return False

    def has_object_permission(self, request, view, obj):
        self.message = 'Метод не доступен'
        return False


class IsShop(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.user.type != 'shop':
                self.message = 'Метод доступен только для магазинов'
                return False
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.type != 'shop':
            self.message = 'Метод доступен только для магазинов'
            return False
        return True
