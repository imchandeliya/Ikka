from rest_framework import serializers
from rest_framework.exceptions import NotAcceptable
from purchase.models import PurchaseModel


class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseModel
        fields = '__all__'