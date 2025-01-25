"""This module contains category information serializer."""

from rest_framework import serializers
from categories.models import Category
from utils import constant

class CategorySerializer(serializers.ModelSerializer):
    """This class implements category information serializer."""

    subcategories = serializers.SerializerMethodField()

    class Meta:
        """This class implements meta class."""

        model = Category
        fields = [
            "id",
            "name",
            "parent_category",
            "description",
            "is_active",
            "subcategories",
        ]

    def get_subcategories(self, obj):
        """This method returns subcategories."""
        subcategories = obj.subcategories.filter(is_deleted=constant.STATUS_FALSE)
        if subcategories.exists():
            return CategorySerializer(subcategories, many=constant.STATUS_TRUE).data
        return []
