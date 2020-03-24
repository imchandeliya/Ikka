from rest_framework import serializers
from rest_framework.exceptions import NotAcceptable
from product.models import ProductModel


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = '__all__'

    # validate attributes
    def validate(self, attrs):
        product_name = str(attrs['product_name'])
        if len(product_name) <= 5:
            raise NotAcceptable('product name should be atleast 5 digits')

        try:
            product_cost = int(attrs['cost'])
            if float(product_cost) <= 0:
                raise NotAcceptable('cost cannot be 0 or negative')
        except:
            raise NotAcceptable('cost must be a number')

        ProductSerializer.checkExistingProductName(self, attrs)
        return attrs

    # check if there are existing products in the company with same name
    def checkExistingProductName(self, data):
        product_name_raw = data['product_name']
        company = data['company']

        product_list = ProductModel.objects.filter(product_name=product_name_raw, company=company)
        if len(product_list) > 0:
            raise NotAcceptable("product already present:" + str(product_list[0].product_name) + ", cost" + str(
                product_list[0].cost))

        return data
