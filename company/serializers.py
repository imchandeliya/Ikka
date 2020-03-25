from rest_framework import serializers
from rest_framework.exceptions import NotAcceptable
from .models import CompanyModel


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyModel
        fields = '__all__'

    def validate(self, attrs):
        CompanySerializer.validate_company_name(self, attrs['company_name'])
        CompanySerializer.validate_gst_number(self, attrs['gst_number'])
        return attrs

    # Validate company name
    def validate_company_name(self, data):
        company_name = str(data)
        # raise NotAcceptable('company, length:' + str(company_name) + ", length:" + str(len(company_name)))
        if 5 >= len(company_name):
            raise NotAcceptable('Company Name cannot be less than 5 characters, company:' + str(company_name))
        if len(company_name) >= 100:
            raise NotAcceptable('Company Name cannot be more than 100 characters, company:' + str(company_name))

        return data

    # validate GSTIN number
    def validate_gst_number(self, data):
        gst_number = str(data)
        if len(gst_number) != 15:
            raise NotAcceptable('GST number must be of 15 digits only, your length: ' + str(len(gst_number)))
        return data

