from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .forms import *
from .models import *

from django.contrib.auth.mixins import LoginRequiredMixin
from users.mixins import PermissionsRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from datetime import datetime
from django.db.models import F

#Prestamo
class PrestamoList(PermissionsRequiredMixin, LoginRequiredMixin, ListView):
    model = Prestamos
    template_name = 'prestamos/prestamos_list.html'
    required_permissions = ('prestamos.add_prestamos',)

    def get_queryset(self):
        return Prestamos.objects.find(self.request.GET.get('q', False)).filter(estado=1).order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q', '')
        return context


class PrestamoCreate(PermissionsRequiredMixin, LoginRequiredMixin, CreateView):
    model = Prestamos
    form_class = PrestamoForm
    template_name = 'prestamos/prestamos_create.html'
    success_url = reverse_lazy('prestamos:prestamo_listar')
    required_permissions = ('prestamos.add_prestamos',)


class PrestamoUpdate(PermissionsRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Prestamos
    form_class = PrestamoEditForm
    template_name = 'prestamos/prestamos_update.html'
    success_url = reverse_lazy('prestamos:prestamo_listar')
    required_permissions = ('prestamos.change_prestamos',)


class PrestamoDelete(PermissionsRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Prestamos
    template_name = 'prestamos/prestamos_delete.html'
    success_url = reverse_lazy('prestamos:prestamo_listar')
    required_permissions = ('prestamos.delete_prestamos',)


class Devolucion(PermissionsRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Prestamos
    form_class = DevolucionForm
    template_name = 'prestamos/devoluciones.html'
    success_url = reverse_lazy('prestamos:prestamo_listar')
    required_permissions = ('prestamos.change_prestamos',)


class DevolucionList(PermissionsRequiredMixin, LoginRequiredMixin, ListView):
    model = Prestamos
    template_name = 'prestamos/devoluciones_list.html'
    required_permissions = ('prestamos.add_prestamos',)

    # def get_queryset(self, *args, **kwargs):
    #     return Prestamos.objects.filter(estado=0).order_by('-id')
    def get_queryset(self):
        return Prestamos.objects.find(self.request.GET.get('q', False)).filter(estado=0).order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q', '')
        return context


class RetrasosList(PermissionsRequiredMixin, LoginRequiredMixin, ListView):
    model = Prestamos
    template_name = 'prestamos/retrasos.html'
    required_permissions = ('prestamos.add_prestamos',)

    def get_queryset(self):
        return Prestamos.objects.filter(fecha_devolucion__lt=F('fecha_actual')).order_by('-id')
        #return Prestamos.objects.filter(fecha_devolucion__lt='2018-06-27 02:00:35-04').order_by('-id')


class DanosList(PermissionsRequiredMixin, LoginRequiredMixin, ListView):
    model = Prestamos
    template_name = 'prestamos/danos.html'
    required_permissions = ('prestamos.add_prestamos',)

    def get_queryset(self):
        return Prestamos.objects.filter(estado_entrega=0).order_by('-id')


def prestamo_activo(request):

    obj = Prestamos.objects.filter(estado=1).order_by('-id')

    for abc in obj:
        obj_usuario = abc.id_usuario,
        obj_producto = abc.id_producto,
        obj_fechaDevol = abc.fecha_devolucion,

    context = {
        "obj": obj,
        "obj_usuario": obj_usuario,
        "obj_producto": obj_producto,
        "obj_fechaDevol": obj_fechaDevol,
    }

    return render(request, "prestamos/list_prestamos.html", context)


def prestamo_atrasado(request):

    obj = Prestamos.objects.filter(fecha_devolucion__lte=datetime.now(), estado=1).order_by('-id')
    for abc in obj:
        obj_usuario = abc.id_usuario,
        obj_producto = abc.id_producto,
        obj_fechaDevol = abc.fecha_devolucion,

    context = {
        "obj": obj,
        "obj_usuario": obj_usuario,
        "obj_producto": obj_producto,
        "obj_fechaDevol": obj_fechaDevol,

    }

    return render(request, "prestamos/list_prestamos_atrasado.html", context)

