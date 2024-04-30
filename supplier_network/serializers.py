from rest_framework import serializers
from rest_framework.exceptions import PermissionDenied

from supplier_network.models import SupplierNetwork


class SupplierNetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplierNetwork
        exclude = ['owner', ]

    def create(self, validated_data):
        validated_data['owner'] = self.context['request'].user
        instance = self.Meta.model.objects.create(**validated_data)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        if self.context['request'].user == instance.owner:
            instance.arrears = validated_data.get('arrears', instance.arrears)
            instance.save()
            return instance
        else:
            raise PermissionDenied("You are not allowed to update arrears for this instance.")
