"""This module contains the TaskSerializer class which is used to serialize the Task model."""

from rest_framework import serializers
from tasks.models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Task serializer class which is used to serialize the Task model."""

    class Meta:
        """Meta class to define the model and fields to serialize."""

        model = Task
        fields = [
            "id",
            "product",
            "title",
            "description",
            "status",
            "assigned_user",
            "due_date",
        ]
