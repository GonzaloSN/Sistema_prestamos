# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-26 21:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mantenedor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prestamos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('estado', models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default=1, max_length=100)),
                ('fecha_prestamo', models.DateTimeField()),
                ('fecha_devolucion', models.DateTimeField()),
                ('observaciones', models.CharField(max_length=200)),
                ('fecha_actual', models.DateTimeField(auto_now_add=True)),
                ('estado_entrega', models.CharField(choices=[('1', 'Sin Detalles'), ('0', 'Con Detalles')], default='', max_length=200)),
                ('observaciones_devolucion', models.CharField(max_length=200)),
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mantenedor.Producto')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
