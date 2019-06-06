import datetime
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView,CreateView,UpdateView,ListView
from .models import Laboratorio
from .forms import LaboratorioForm, LaboratorioEditForm
from django.contrib.auth.mixins import LoginRequiredMixin
from users.mixins import PermissionsRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.forms.models import model_to_dict
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import Http404
from django.core.serializers.json import DjangoJSONEncoder
import json
from django.contrib.auth.models import User
from django.core import serializers


class LaboratorioView(TemplateView, LoginRequiredMixin):
    template_name = 'laboratorio/calendar.html'
    forms_class = LaboratorioForm


    def get_context_data(self, **kwargs):
        context = super(LaboratorioView, self).get_context_data(**kwargs)
        context['eventlist'] = Laboratorio.objects.all().values('id', 'usuario__username', 'title', 'start', 'end')
        return context


class LaboratorioCreate(PermissionsRequiredMixin, LoginRequiredMixin, CreateView):
    model = Laboratorio
    form_class = LaboratorioForm
    template_name = 'laboratorio/laboratorio_modal.html'
    success_url = reverse_lazy('laboratorio:calendar')
    required_permissions = ('laboratorio.add_laboratorio')


class LaboratorioUpdate(PermissionsRequiredMixin,LoginRequiredMixin,UpdateView):
    model = Laboratorio
    form_class = LaboratorioEditForm
    template_name = 'laboratorio/laboratorio_edit_modal.html'
    required_permissions = ('laboratorio.change_laboratorio')

    def get_id(self, **kwargs):
        lab = Laboratorio.objects.get(id=kwargs['pk'])
        return lab

def reserva(request):

    obj = Laboratorio.objects.all()
    for abc in obj:
        obj_usuario = abc.usuario,
        obj_nombre = abc.nombre,
        obj_fechaInicio = abc.fechaInicio,
        obj_fechaTermino = abc.fechaTermino,


    context = {
        "obj": obj,
        "obj_usuario": obj_usuario,
        "obj_nombre" : obj_nombre,
        "obj_fechaInicio" : obj_fechaInicio,
        "obj_fechaTermino" : obj_fechaTermino,
    }

    return render(request, "laboratorio/list_reserva.html", context)

