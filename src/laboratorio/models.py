from django.db import models
from django.contrib.auth.models import User


class Laboratorio(models.Model):
    id = models.AutoField(primary_key=True,unique=True)
    usuario = models.ForeignKey(User)
    title = models.CharField(max_length=100)
    start = models.DateTimeField()
    end = models.DateTimeField()
    #observacion = models.CharField(max_length=100)

    def __str__(self):
        return self.title




# Create your models here.
