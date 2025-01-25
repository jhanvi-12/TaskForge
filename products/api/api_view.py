from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from products.models import Product
from products.api.serializer import ProductSerializer
from users.permissions import IsAdminUserOrReadOnly

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsAdminUserOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.request.query_params.get('category')
        is_active = self.request.query_params.get('is_active')
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        if is_active:
            queryset = queryset.filter(is_active=is_active.lower() == 'true')
        return queryset

    def perform_destroy(self, instance):
        instance.soft_delete()