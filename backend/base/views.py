from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from .products import products

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
    return Response(products)

@api_view(['GET'])
def get_product(request, pk):
    
    for p in products:
        if p['_id'] == pk:
            return Response(p)
    return Response('no product found')