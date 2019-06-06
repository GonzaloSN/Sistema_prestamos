from django import forms
from .models import *


class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto

        fields = [
            'codigo',
            'marca',
            'descripcion',
            'id_categoria_id',
            'estado'
        ]
        labels = {
            'codigo': 'Codigo',
            'marca': 'Marca',
            'estado': 'Estado',
            'descripcion': 'Descripcion',
            'id_categoria_id': 'Categoria'
        }
        widgets = {
            'codigo':  forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Puede incluir hasta 100 caracteres'}),
            'marca': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese marca'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ingrese descripcion', 'rows': 3}),
            'id_categoria_id': forms.Select(attrs={'class': 'form-control'}),

        }


class ProductoEstadoForm(forms.ModelForm):

    class Meta:
        model = Producto

        fields = [
            'estado'
        ]
        labels = {
            'estado': 'Estado'
        }
        widgets = {
            'estado': forms.TextInput(attrs={'class': 'form-control'})

        }


class CategoriaForm(forms.ModelForm):

    class Meta:
        model = Categoria

        fields = [
            'nombre'
        ]
        labels = {
            'nombre': 'Nombre'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese nombre'})
        }



