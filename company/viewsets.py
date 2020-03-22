from rest_framework import viewsets
from . import serializers
from . import models


class CompanyViewSet(viewsets.ModelViewSet):
    """
    API endpoint
    """
    queryset = models.CompanyModel.objects.all()
    serializer_class = serializers.CompanySerializer