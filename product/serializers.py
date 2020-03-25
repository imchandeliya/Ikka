from rest_framework import serializers
from rest_framework.exceptions import NotAcceptable
from product.models import ProductModel


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = '__all__'

    # validate attributes
    def validate(self, attrs):
        ProductSerializer.validate_product_name(self, attrs['product_name'])
        ProductSerializer.validate_product_cost(self, attrs['cost'])
        return attrs

    def validate_product_name(self, data):
        product_name = str(data)
        if len(product_name) <= 5:
            raise NotAcceptable('product name should be atleast 5 digits')
        return data

    def validate_product_cost(self, data):
        try:
            product_cost = int(data)
            if float(product_cost) <= 0:
                raise NotAcceptable('cost cannot be 0 or negative')
        except NotAcceptable:
            raise NotAcceptable('cost must be a number')

        return data


    # check if there are existing products in the company with same name
    def check_existing_product_name(data):
        product_name_raw = data['product_name']
        product_list = ProductModel.objects.filter(product_name=product_name_raw)
        if len(product_list) > 0:
            raise NotAcceptable("product already present:" + str(product_list[0].product_name) + ", cost" + str(
                product_list[0].cost))

        return data
