from django.db import models

# Create your models here.
from company.models import CompanyModel


class ProductModel(models.Model):
    product_name = models.CharField(max_length=98, unique=True, null=False)
    company = models.ForeignKey(CompanyModel, on_delete=models.CASCADE)
    cost = models.IntegerField(null=False, default=0)

    class Meta:
        db_table = r'product'
