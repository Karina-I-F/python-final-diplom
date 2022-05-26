from rest_framework import permissions


class DenyAny(permissions.BasePermission):
    def has_permission(self, request, view):
        self.message = 'Method are not allowed'
        return False

    def has_object_permission(self, request, view, obj):
        self.message = 'Method are not allowed'
        return False
