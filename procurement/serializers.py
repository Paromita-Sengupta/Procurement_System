from rest_framework import serializers
from procurement.models import Component, Supplier


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        exclude = ('created', 'updated')


class ComponentSerializer(serializers.ModelSerializer):
    text = serializers.CharField(source='__str__', read_only=True)
    suppliers = SupplierSerializer(many=True, read_only=True)

    class Meta:
        model = Component
        exclude = ('created', 'updated')
