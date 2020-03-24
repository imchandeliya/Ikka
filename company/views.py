from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status
from .models import CompanyModel
from .serializers import CompanySerializer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def company(request):
    if request.method == 'GET':
        company = CompanyModel.objects.all()
        serializer = CompanySerializer(company, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        json_parser = JSONParser()
        data = json_parser.parse(request)
        serializer = CompanySerializer(data=data)

        if serializer.is_valid():
            serializer.validate(data)
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)