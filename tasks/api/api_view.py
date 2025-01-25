"""This module is responsible for the tasks related API viwes."""

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from tasks.models import Task
from tasks.api.serializer import TaskSerializer


class TaskViewSet(ModelViewSet):
    """Task view set which is used to retrieve tasks."""

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Filter tasks based on the assigned user."""
        user = self.request.user
        queryset = Task.objects.filter(is_deleted=False, assigned_user=user)
        status = self.request.query_params.get('status')
        product_id = self.request.query_params.get('product')
        if status:
            queryset = queryset.filter(status=status)
        if product_id:
            queryset = queryset.filter(product_id=product_id)
        return queryset

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user, partial=True)

    def perform_destroy(self, instance):
        instance.soft_delete()
