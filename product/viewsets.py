from rest_framework import viewsets
from . import serializers
from . import models


class ProductViewSet(viewsets.ModelViewSet):
    """API endpoint"""

    queryset = models.ProductModel.objects.all()
    serializer_class = serializers.ProductSerializer