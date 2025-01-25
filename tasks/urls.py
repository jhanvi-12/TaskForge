"""This module defines the URL patterns for the tasks app."""

from rest_framework.routers import DefaultRouter
from tasks.api.api_view import TaskViewSet

router = DefaultRouter()
router.register('', TaskViewSet, basename='task')

urlpatterns = router.urls