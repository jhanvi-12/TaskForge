from django.db import models
from products.models import Product
from django.conf import settings
from core.models import SoftDeleteModel


# Create your models here.
class Task(SoftDeleteModel, models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("inprogress", "In Progress"),
        ("completed", "Completed"),
    ]
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="tasks")
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
    )
    assigned_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="tasks"
    )
    due_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id, self.product, self.title}"
