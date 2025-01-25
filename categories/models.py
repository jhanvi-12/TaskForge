"""This module is used to implement categories model."""

from django.db import models
from django.conf import settings
from core.models import SoftDeleteModel

# Create your models here.
class Category(SoftDeleteModel, models.Model):
    """This model is used to represent a category."""
    name = models.CharField(max_length=255)
    parent_category = models.ForeignKey(
        'self', on_delete=models.SET_NULL, null=True, blank=True, related_name='subcategories'
    )
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='created_categories'
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='updated_categories', null=True, blank=True
    )

    def __str__(self):
        return f"{self.id, self.name, self.parent_category}"
