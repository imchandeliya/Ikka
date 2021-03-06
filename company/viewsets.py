from rest_framework import viewsets

from . import models
from . import serializers


class CompanyViewSet(viewsets.ModelViewSet):
    """
    API endpoint
    """
    queryset = models.CompanyModel.objects.all()
    serializer_class = serializers.CompanySerializer
