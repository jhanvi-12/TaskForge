from rest_framework.routers import DefaultRouter
from products.api.api_view import ProductViewSet

router = DefaultRouter()
router.register('', ProductViewSet, basename='product')

urlpatterns = router.urls
