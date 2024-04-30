from rest_framework.routers import DefaultRouter

from products import apps
from products.views import ProductViewSet

app_name = apps.ProductsConfig.name

router = DefaultRouter()
router.register('products', ProductViewSet, basename='products')

urlpatterns = router.urls
