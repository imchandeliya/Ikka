from company import viewsets
from rest_framework import routers

router = routers.DefaultRouter()
router.register(prefix=r'company', viewset=viewsets.CompanyViewSet, basename='company')
