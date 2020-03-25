from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status
from .models import ProductModel
from .models import CompanyModel
from .serializers import ProductSerializer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.exceptions import NotFound

# Create your views here.

# def check_if_company_presents(data):
#     company_raw = data['company']
#     company = CompanyModel.objects.get(company_raw)
#     raise NotFound('company name', str(company.company_name))
#     if company is None:
#         raise NotFound('company not found by provided company id')
#     return data

@csrf_exempt
def product(request):
    if request.method == 'GET':
        product = ProductModel.objects.all()
        serializer = ProductSerializer(product, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        json_parser = JSONParser()
        data = json_parser.parse(request)
        serializer = ProductSerializer(data=data)

        if serializer.is_valid():
            serializer.validate(data)
            # check_if_company_presents(data)
            ProductSerializer.check_existing_product_name(data)
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
