from django.db import models

# Create your models here.
from company.models import CompanyModel
from product.models import ProductModel


class PurchaseModel(models.Model):
    order_number = models.CharField(max_length=12)
    company = models.ForeignKey(CompanyModel, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    rate = models.IntegerField(null=False, default=0)
    quantity = models.IntegerField(null=False, default=0)
    total_price = models.IntegerField(null=False, default=0)

    class Meta:
        db_table = r'purchase'
