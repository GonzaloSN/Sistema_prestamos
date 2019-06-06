from django.db import models
from mantenedor.models import Producto
from django.contrib.auth.models import User
from django.db.models import Q

# Create your models here.


class PrestamoManager(models.Manager):

    def find(self, search):
        if not search:
            return self

        qs = Q(id_usuario__username__icontains=search) | \
             Q(id_producto__codigo__icontains=search)

        return self.filter(qs)


class Prestamos(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    id_usuario = models.ForeignKey(User)
    id_producto = models.ForeignKey('mantenedor.Producto')
    estado = models.CharField(max_length=100, default=1, choices=(('1', 'Activo'), ('0', 'Inactivo')))
    fecha_prestamo = models.DateTimeField()
    fecha_devolucion = models.DateTimeField()
    observaciones = models.CharField(max_length=200)
    fecha_actual = models.DateTimeField(auto_now_add=True, auto_now=False)
    estado_entrega = models.CharField(max_length=200, default="", choices=(('1', 'Sin Detalles'), ('0', 'Con Detalles')))
    observaciones_devolucion = models.CharField(max_length=200)

    objects = PrestamoManager()

    def __str__(self):
        return self.observaciones