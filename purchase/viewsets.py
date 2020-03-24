from rest_framework import viewsets
from rest_framework.exceptions import NotAcceptable
from . import serializers
from . import models


class PurchaseViewSet(viewsets.ModelViewSet):
    """API endpoint"""

    queryset = models.PurchaseModel.objects.all()
    serializer_class = serializers.PurchaseSerializer

    