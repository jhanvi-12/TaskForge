"""This file is used to register the CustomUser model with the Django admin site."""

from django.contrib import admin
from users.models import CustomUser

# Register your models here.
admin.site.register(CustomUser)
