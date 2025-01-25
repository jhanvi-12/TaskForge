from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from categories.models import Category
from categories.api.serializer import CategorySerializer
from users.permissions import IsAdminUserOrReadOnly

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated, IsAdminUserOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)

    def perform_destroy(self, instance):
        instance.soft_delete()