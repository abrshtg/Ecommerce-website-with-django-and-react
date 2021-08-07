from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.serializers import Serializer
# from .products import products

from .models import Product
from .serializers import ProductSerializer

@api_view(['GET'])
def get_route(request):
    route = [
        '/api/products/',
        '/api/products/upload',
        '/api/products/<id>/reviews/',
        '/api/products/top/',
        '/api/products/<id>/',
        '/api/products/delete/<id>/',
        '/api/products/<update>/<id>/'
    ]
    return Response(route)

@api_view(['GET'])
def get_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_product(request, pk):
    try:
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product, many=False)
        return Response(serializer.data)
    
    except:
        return Response('item not found: ')
    # for p in products:
    #     if p['_id'] == pk:
    #         return Response(p)
    # return Response('no product found')