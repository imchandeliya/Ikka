from company.viewsets import CompanyViewSet
from product.viewsets import ProductViewSet
from purchase.viewsets import PurchaseViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(prefix=r'company', viewset=CompanyViewSet)
router.register(prefix=r'product', viewset=ProductViewSet)
router.register(prefix=r'purchase', viewset=PurchaseViewSet)