from rest_framework import serializers
from rest_framework.exceptions import NotAcceptable
from .models import CompanyModel


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyModel
        fields = '__all__'

    # Validate company name
    def validate_company_name(self, value):
        company_name = str(value)
        if 5 >= len(company_name) >= 100:
            raise NotAcceptable('Company Name cannot be less than 5 letter, company:' + company_name)
        return value

    # validate GSTIN number
    def validate_gst_number(self, value):
        gst_number = str(value)
        if len(gst_number) != 15:
            raise NotAcceptable('GST number must be of 15 digits only')
        return value

