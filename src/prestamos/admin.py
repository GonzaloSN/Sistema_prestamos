from django.contrib import admin
from .models import *
from .models import Prestamos
from .fields import UserSelectWidget
from django import forms
from .forms import *
from datetimewidget.widgets import DateWidget
# Register your models here.


class adminPrestamos(admin.ModelAdmin):
    form = PrestamoForm
    list_display = ["fecha_prestamo", "fecha_devolucion", "observaciones"]
    list_filter = ["id"]
    search_fields = ["fecha_prestamo"]

    class Meta:
        model = Prestamos

admin.site.register(Prestamos, adminPrestamos)
