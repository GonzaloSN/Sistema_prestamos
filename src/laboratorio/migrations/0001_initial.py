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
    ]

    operations = [
        migrations.CreateModel(
            name='Laboratorio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=100)),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]