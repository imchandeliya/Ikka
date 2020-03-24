from django.http import HttpResponse
from django import forms
from rest_framework import viewsets, status
from rest_framework.response import Response
from . import serializers
from . import models


class CompanyViewSet(viewsets.ModelViewSet):
    """
    API endpoint
    """
    queryset = models.CompanyModel.objects.all()
    serializer_class = serializers.CompanySerializer