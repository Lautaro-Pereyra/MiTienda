from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nombre
    

class Producto (models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    image = CloudinaryField('image', default='')
    Categoria = models.ForeignKey(Categoria, 
                                  related_name='productos',
                                  on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nombre
    

class Cliente(models.Model):
    nombre = models.CharField(max_length=80)
    email = models.EmailField(max_length=100)
    telefono = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.nombre
