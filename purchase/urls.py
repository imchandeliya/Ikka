from django.urls import path
from purchase.views import *

urlpatterns = [
    path('purchase/', purchase)
]