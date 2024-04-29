from django.contrib import admin

from supplier_network.models import SupplierNetwork


@admin.register(SupplierNetwork)
class SupplierNetworkAdmin(admin.ModelAdmin):
    pass
