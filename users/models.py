"""This module contains admin and users related model information"""

from django.contrib.auth.models import AbstractUser
from django.db import models

from utils import constant

# Create your models here.

class CustomUser(AbstractUser):
    """Custom user model class for admin and normal users"""
    is_admin = models.BooleanField(default=constant.STATUS_FALSE)

    def __str__(self):
        """Return username and email"""
        return f"{self.id, self.username}, {self.email}"