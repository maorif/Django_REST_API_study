import json
from django.forms.models import model_to_dict
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer

from products.models import Product

@api_view(["GET"])
def api_home(request, *args, **kwargs):
    """
    DRF (Django Rest Framework) API VIEW
    """

    instance = Product.objects.all().order_by("?").last()
    data = {}

    if instance:
        # data = model_to_dict(instance, fields=['id', 'name', 'description', 'price'])
        data = ProductSerializer(instance).data
        print(data)

    return Response(data)

@api_view(["POST"])
def api_create_product(request, *args, **kwargs):
  
    serializer = ProductSerializer(data=request.data)
    
    if serializer.is_valid(raise_exception=True):
        instance = serializer.save()
        print(instance)
        print(serializer.data)
        data = serializer.data

        return Response(data)
    
    return Response({"message": "invalid data."}, status=400)