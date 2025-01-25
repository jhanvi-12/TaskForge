from rest_framework.routers import DefaultRouter
from categories.api.api_view import CategoryViewSet

router = DefaultRouter()
router.register('', CategoryViewSet, basename='category')

urlpatterns = router.urls
