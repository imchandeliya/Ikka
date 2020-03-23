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

    # def create(self, request, *args, **kwargs):
    #
    #     CompanyViewSet.create()
    #     super(CompanyViewSet, self).create(request, args, kwargs)
    #     response = {"status_code": status.HTTP_200_OK,
    #                 "message": "Successfully created",
    #                 "result": request.data}
    #     return Response(response)
