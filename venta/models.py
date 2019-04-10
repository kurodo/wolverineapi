from django.db import models
from catalogo.models import ProdcutoVariacion

TIPO_VENTA=(
    ('bol', 'Boleta'),
    ('fac', 'Factura'),
    ('nn', 'Ninguna'),
)


# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    ruc = models.CharField(max_length=12, blank = True)
    direccion = models.CharField(max_length=200, blank = True)
    telefono = models.CharField(max_length=20, blank = True)
    correo = models.CharField(max_length=100, blank = True)
    comentario = models.TextField(max_length=100, blank = True)
    def __str__(self):
        return self.nombre

class Venta(models.Model):
    fecha = models.DateTimeField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    monto = models.IntegerField()
    tipo = models.CharField(max_length=3, choices=TIPO_VENTA)
    registro = models.BooleanField(default=False)

class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(ProdcutoVariacion, on_delete=models.CASCADE)
    precio = models.IntegerField()
    cantidad = models.IntegerField()
    unidad_venta = models.CharField(max_length=100)
    total = models.IntegerField()
