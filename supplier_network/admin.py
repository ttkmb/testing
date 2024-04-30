from django.contrib import admin
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils.safestring import mark_safe

from supplier_network.models import SupplierNetwork


@admin.register(SupplierNetwork)
class SupplierNetworkAdmin(admin.ModelAdmin):
    raw_id_fields = ('supplier',)
    list_display = ['name', 'arrears', 'supplier_url', 'country', 'city']
    list_filter = ['city']
    actions = ['clear_arrears']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'supplier' and request.resolver_match.url_name == 'change':
            current_object_id = request.resolver_match.kwargs['object_id']
            current_object = SupplierNetwork.objects.get(id=current_object_id)

            def limit_suppliers_choices():
                queryset = SupplierNetwork.objects.exclude(id=current_object.id)
                kwargs['queryset'] = queryset
                return kwargs

            kwargs = limit_suppliers_choices()

        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    @admin.display(description='Поставщик')
    def supplier_url(self, obj):
        if obj.supplier:
            url = reverse('admin:supplier_network_suppliernetwork_change', args=[obj.supplier.id])
            return mark_safe('<a href="{}">{}</a>'.format(url, obj.supplier))
        else:
            return '0 уровень иерархии - Завод'

    @admin.action(description='Очистить задолженность перед поставщиком')
    def clear_arrears(self, request, queryset):
        queryset.update(arrears=0)

