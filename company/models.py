from django.db import models


# Create your models here.
class CompanyModel(models.Model):
    company_id = models.CharField
    company_name = models.CharField(max_length=100)
    gst_number = models.CharField(max_length=15)
    address = models.CharField(max_length=200)

    class Meta:
        db_table = r'company'
