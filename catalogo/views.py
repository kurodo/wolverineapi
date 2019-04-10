from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProductoSerializer, PrecioProductoSerializer, VariacionSerializer, ProdcutoVariacionSerializer
from .models import Producto, PrecioProducto, Variacion, ProdcutoVariacion

# Create your views here.
class ProductoViewSet(viewsets.ModelViewSet):
    serializer_class = ProductoSerializer
    queryset = Producto.objects.all()

class PrecioProductoViewSet(viewsets.ModelViewSet):
    serializer_class = PrecioProductoSerializer
    queryset = PrecioProducto.objects.all()

class VariacionViewSet(viewsets.ModelViewSet):
    serializer_class = VariacionSerializer
    queryset = Variacion.objects.all()

class ProdcutoVariacionViewSet(viewsets.ModelViewSet):
    serializer_class = ProdcutoVariacionSerializer
    queryset = ProdcutoVariacion.objects.all()
