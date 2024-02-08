from django.db import models

# Create your models here.
from store.info import TALLAS


class Marca(models.Model):
    nombre = models.CharField(max_length=255)
    referencia = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.nombre


class Producto(models.Model):

    nombre = models.CharField(max_length=255)
    talla = models.CharField(max_length=1, choices=TALLAS)
    observaciones = models.TextField()
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    cantidad_inventario = models.IntegerField()
    fecha_embarque = models.DateField()

    def __str__(self):
        return self.nombre
