"""
Custom permission classes for the Task and Product Management system.

This module contains custom permission classes for user-related functionalities.
"""

from rest_framework.permissions import BasePermission


class IsAdminUserOrReadOnly(BasePermission):
    """
    Custom permission to only allow admin users to edit objects.
    Read-only permissions are allowed for any request.
    """

    def has_permission(self, request, view):
        """
        Check if the request has permission to proceed.

        Allow read-only methods for any request.
        Allow write methods only for authenticated admin users.
        """
        if request.method in ["GET", "HEAD", "OPTIONS"]:
            return True
        return request.user.is_authenticated and request.user.is_admin
