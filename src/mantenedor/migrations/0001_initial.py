# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-26 21:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('codigo', models.CharField(max_length=100)),
                ('marca', models.CharField(default='', max_length=100)),
                ('descripcion', models.CharField(blank=True, max_length=100, null=True)),
                ('estado', models.CharField(choices=[('1', 'Disponible'), ('0', 'Dado de Baja'), ('2', 'En Mantención')], default=1, max_length=100)),
                ('id_categoria_id', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='mantenedor.Categoria')),
            ],
        ),
    ]