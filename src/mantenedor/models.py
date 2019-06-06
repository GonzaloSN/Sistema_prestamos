from django.db import models
#from mantenedor.models import Categoria
from django.db.models import Q

# Create your models here.


class Categoria(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    nombre = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.nombre


class ProductoManager(models.Manager):

    def find(self, search):
        if not search:
            return self

        qs = Q(codigo__icontains=search) | \
             Q(marca__icontains=search) | \
             Q(descripcion__icontains=search)

        return self.filter(qs)


class Producto(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    codigo = models.CharField(max_length=100, blank=False, null=False)
    marca = models.CharField(max_length=100, blank=False, null=False, default="")
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    id_categoria_id = models.ForeignKey(Categoria, blank=True, null=True, default=1)
    estado = models.CharField(max_length=100, blank=False, null=False,default=1, choices=(('1', 'Disponible'), ('0', 'Dado de Baja'), ('2', 'En Mantención')))

    objects = ProductoManager()

    def __str__(self):
        return self.codigo




