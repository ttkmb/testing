from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from supplier_network.models import SupplierNetwork
from supplier_network.permissions import IsActive
from supplier_network.serializers import SupplierNetworkSerializer


class SupplierViewSet(ModelViewSet):
    queryset = SupplierNetwork.objects.all()
    serializer_class = SupplierNetworkSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['country']
    permission_classes = [IsActive]
