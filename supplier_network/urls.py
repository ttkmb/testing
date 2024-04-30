from rest_framework import routers
from .views import SupplierViewSet

router = routers.DefaultRouter()
router.register(r'suppliers', SupplierViewSet, basename='suppliers')

urlpatterns = router.urls
