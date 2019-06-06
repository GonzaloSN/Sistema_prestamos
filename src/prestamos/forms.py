from .models import *
from django import forms
from datetimewidget.widgets import DateTimeWidget
from .fields import UserSelectWidget
from django_select2.forms import Select2Widget
from django.contrib.auth.models import User
from mantenedor.models import Producto
from django.forms import ModelChoiceField


class PrestamoForm(forms.ModelForm):
    inner_qs = Prestamos.objects.filter(estado=1).values('id_producto_id')
    id_producto = forms.ModelChoiceField(queryset=Producto.objects.exclude(id__in=inner_qs).filter(estado=1), label='Producto')

    class Meta:
        model = Prestamos
        exclude = ['fecha_actual', 'estado_entrega', 'observaciones_devolucion']

        fields = [
            'id_usuario',
            'id_producto',
            'estado',
            'fecha_prestamo',
            'fecha_devolucion',
            'observaciones',
        ]
        labels = {
            'id_usuario': 'Usuario',
            'id_producto': 'Producto',
            'estado': 'Estado',
            'fecha_prestamo': 'Fecha Prestamo',
            'fecha_devolucion': 'Fecha Devolucion',
            'observaciones': 'Observaciones',
        }

        widgets = {
            'id_usuario': forms.Select(attrs={'class': 'form-control', 'id': 'usuario'}),
            'id_producto': forms.Select(attrs={'class': 'form-control', 'id': 'productos'}),
            'estado': forms.Select(attrs={'class': 'form-control', 'id': 'estadoPrestamo'}),
            'fecha_prestamo': DateTimeWidget(attrs={'id': "fecha_prestamo"}, usel10n=True, bootstrap_version=3),
            'fecha_devolucion': DateTimeWidget(attrs={'id': "fecha_devolucion"}, usel10n=True, bootstrap_version=3),
            'observaciones': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ingrese Observacion', 'rows': 3}),
        }


class PrestamoEditForm(forms.ModelForm):

    class Meta:
        model = Prestamos
        exclude = ['id_usuario', 'id_producto', 'estado']

        fields = [
            'fecha_prestamo',
            'fecha_devolucion',
            'observaciones',
        ]
        labels = {
            'fecha_prestamo': 'Fecha Prestamo',
            'fecha_devolucion': 'Fecha Devolucion',
            'observaciones': 'Observaciones',
        }

        widgets = {
            'fecha_prestamo': DateTimeWidget(attrs={'id': "fecha_prestamo"}, usel10n=True, bootstrap_version=3),
            'fecha_devolucion': DateTimeWidget(attrs={'id': "fecha_devolucion"}, usel10n=True, bootstrap_version=3),
            'observaciones': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ingrese Observacion', 'rows': 3}),
        }


class DevolucionForm(forms.ModelForm):

    class Meta:
        model = Prestamos
        exclude = ['id_usuario', 'id_producto', 'fecha_prestamo', 'fecha_devolucion', 'observaciones']

        fields = [
            #'fecha_actual',
            'estado',
            'estado_entrega',
            'observaciones_devolucion'
        ]
        labels = {
            'estado': 'Estado de Prestamo',
            #'fecha_actual': 'Fecha Actual',
            'estado_entrega': 'Estado Devolucion',
            'observaciones_devolucion': 'Observaciones al Prestamo'
        }

        widgets = {
            #'fecha_actual': DateTimeWidget(attrs={'id': "fecha_prestamo"}, usel10n=True, bootstrap_version=3),
            'estado': forms.Select(attrs={'class': 'form-control', 'autofocus': 'autofocus', 'id': 'estado'}),
            'estado_entrega': forms.Select(attrs={'class': 'form-control'}),
            'observaciones_devolucion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ingrese Observacion', 'rows': 3}),
        }



