from rest_framework import serializers
from rest_framework.exceptions import NotAcceptable
from purchase.models import PurchaseModel
from product.models import ProductModel
from company.models import CompanyModel

class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseModel
        fields = [
            'company',
            'product',
            'quantity',
        ]

    def validate(self, attrs):
        try:
            product_cost = int(attrs['quantity'])
            if int(product_cost) <= 0:
                raise NotAcceptable('quantity cannot be 0 or negative')
        except:
            raise NotAcceptable('cost must be a number')

        company_id = attrs['company'].id
        company = CompanyModel.objects.get(id=company_id)
        if company is None:
            raise NotAcceptable('Selected company is not present, please provide a valid company')

        product_id = attrs['product'].id
        product = ProductModel.objects.get(id=product_id)
        if product is None:
            raise NotAcceptable('Selected product is not present, please provide a valid product')

        #check if the product belongs to the same company
        product_company_id = product.company.id
        if product_company_id != company_id:
            raise NotAcceptable('Selected product doesn\'t belongs to given company')

        raise NotAcceptable("company id :" + str(company_id) + ", product company id:" + str(product_company_id))
        return attrs

    # def create(self, validated_data):
    #
    #     purchase = PurchaseModel(validated_data)
    #     product = ProductModel.objects.get(id=validated_data["product"].id)
    #     purchase.product = product
    #     product_quantity = purchase.quantity
    #     product_price = int(product.cost)
    #     total_price = product_quantity * product_price
    #
    #     raise NotAcceptable('product is :' + str(product.product_name) + ", quantity:" + str(product_quantity) + " price :" + str(product_price) + ", total price" + str(total_price) + ", object:" + str(product))
