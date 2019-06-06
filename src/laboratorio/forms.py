from django import forms
from .models import *
from datetimewidget.widgets import DateTimeInput
from django.contrib.auth.models import User
from datetimewidget.widgets import DateTimeWidget



class LaboratorioForm(forms.ModelForm):
    #usuario = forms.ModelChoiceField(queryset=User.objects.all(), label='Usuariox')

    class Meta:
        model = Laboratorio
        exclude = []

        fields = [
           'usuario',
            'title',
            'start',
            'end',
           # 'observacion',
        ]

        labels = {
            'usuario' : 'Usuario',
            'title' : 'Nombre',
            'start': 'Fecha de Inicio',
            'end': 'Fecha de Termino',
           #'observacion' : 'Observaciones',
        }

        widgets = {
            'usuario': forms.Select(attrs={'class': 'form-control', 'id': 'usuario'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ingrese nombre evento'}),
            'start': DateTimeWidget(attrs={'id': "start"}, usel10n=True, bootstrap_version=3),
            'end': DateTimeWidget(attrs={'id': "end"}, usel10n=True, bootstrap_version=3)
           # 'observacion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ingrese observacion'}),
        }


class LaboratorioEditForm(forms.ModelForm):

    class Meta:
        model = Laboratorio

        fields = [
           'usuario',
            'title',
            'start',
            'end',

           # 'observacion',
        ]

        labels = {
           'usuario' : 'Usuario',
            'title' : 'Nombre',
            'start': 'Fecha de Inicio',
            'end': 'Fecha de Termino',

        }

        widgets = {
            'usuario': forms.Select(attrs={'class': 'form-control', 'disabled' : 'disabled'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ingrese nombre evento', 'disabled' : 'disabled'}),
            'start':  DateTimeInput(attrs={'class': 'form-control' , 'id' : 'inicio', 'disabled' : 'disabled'}),
            'end': DateTimeInput(attrs={'class': 'form-control', 'disabled' : 'disabled'}),

        }

