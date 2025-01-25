"""This module contains admin creation seeder methods"""

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from utils import message

User = get_user_model()


class Command(BaseCommand):
    """This class provides access to the command manager."""

    help = "Create a default admin user"

    def handle(self, *args, **kwargs):
        """This function creates a default admin user"""
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser("admin", "admin@example.com", "password123")
            self.stdout.write(self.style.SUCCESS(message.ADMIN_CREATED))
        else:
            self.stdout.write(self.style.WARNING(message.ADMIN_EXISTS))
