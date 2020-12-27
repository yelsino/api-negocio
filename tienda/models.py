from django.db import models
from django.utils import timezone
# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to='productos', null=True)
    categoria = models.CharField(max_length=50)
    peso = models.IntegerField()
    medida = models.CharField(max_length=30)
    estado = models.BooleanField()
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
