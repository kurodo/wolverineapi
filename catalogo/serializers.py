from rest_framework import serializers
from .models import Producto, PrecioProducto, Variacion, ProdcutoVariacion

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class PrecioProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrecioProducto
        fields = '__all__'

class VariacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variacion
        fields = '__all__'

class ProdcutoVariacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProdcutoVariacion
        fields = '__all__'
