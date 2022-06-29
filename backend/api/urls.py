from django.urls import path

from .views import api_create_product, api_home

urlpatterns = [
    path('', api_home), # localhost:8000/api/
    # path('products/', api_create_product) # localhost:8000/api/products

]