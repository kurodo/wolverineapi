from django.db import models

# Create your models here.
TIPO_PRODUCTO=(
    ('mc', 'Mercadería'),
    ('pt', 'Producto Terminado'),
    ('in', 'Insumo'),
    ('se', 'Servicio'),
    ('ee', 'Envases y embalajes '),
    ('sd', 'Suministros Diversos'),
    ('ot', 'Otros'),
)
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=100)
    descripcion = models.TextField(blank = True)
    imagen = models.ImageField(upload_to="producto", blank = True, null=True)
    tipo = models.CharField(max_length=3, choices=TIPO_PRODUCTO)
    def __str__(self):
        return self.nombre

class PrecioProducto(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    precio = models.IntegerField()
    fecha = models.DateTimeField()
    def __str__(self):
        return self.producto

class Variacion(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    llave = models.CharField(max_length=100)
    valor = models.CharField(max_length=100)
    def __str__(self):
        return "variacion del producto %s" %(self.producto)

class ProdcutoVariacion(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    variaciones = models.ManyToManyField(Variacion)
    imagen =  models.ImageField(upload_to="producto_variacion", blank = True, null=True)

    def __str__(self):
        return self.producto
