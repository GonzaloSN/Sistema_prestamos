from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy
from .forms import *
from .models import *
from django.http import  HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from users.mixins import PermissionsRequiredMixin
from prestamos.models import Prestamos
# Create your views here.

#Producto
class ProductoList(PermissionsRequiredMixin, LoginRequiredMixin, ListView):
    model = Producto
    paginate_by = 10
    template_name = 'mantenedor/producto_list.html'
    required_permissions = ('mantenedor.add_producto',)

    def get_queryset(self):
        inner_qs = Prestamos.objects.filter(estado=1).values('id_producto_id')
        return Producto.objects.find(self.request.GET.get('q', False)).exclude(id__in=inner_qs).filter(estado=1).order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q', '')
        return context


class ProductoCreate(PermissionsRequiredMixin, LoginRequiredMixin, CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'mantenedor/producto_create.html'
    success_url = reverse_lazy('mantenedor:producto_listar')
    success_message = 'Producto creado exitosamente'
    required_permissions = ('mantenedor.add_producto',)


class ProductoUpdate(PermissionsRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'mantenedor/producto_update.html'
    success_url = reverse_lazy('mantenedor:producto_listar')
    required_permissions = ('mantenedor.change_producto',)


class ProductoEstado(PermissionsRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Producto
    form_class = ProductoEstadoForm
    template_name = 'mantenedor/cambiar_estado.html'
    success_url = reverse_lazy('mantenedor:producto_listar')
    required_permissions = ('mantenedor.change_producto',)


class ProductoDeBajaList(PermissionsRequiredMixin, LoginRequiredMixin, ListView):
    model = Producto
    template_name = 'mantenedor/productos_baja_list.html'
    required_permissions = ('prestamos.add_prestamo',)

    def get_queryset(self):
        return Producto.objects.find(self.request.GET.get('q', False)).filter(estado=0).order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q', '')
        return context


class ProductoMantencionList(PermissionsRequiredMixin, LoginRequiredMixin, ListView):
    model = Producto
    template_name = 'mantenedor/productos_mantencion_list.html'
    required_permissions = ('prestamos.add_prestamo',)

    def get_queryset(self):
        return Producto.objects.find(self.request.GET.get('q', False)).filter(estado=2).order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q', '')
        return context

# class ProductoDelete(PermissionsRequiredMixin, LoginRequiredMixin, DeleteView):
#     model = Producto
#     template_name = 'mantenedor/producto_delete.html'
#     success_url = reverse_lazy('mantenedor:producto_listar')
#     required_permissions = ('mantenedor.delete_producto',)

#Categoria
class CategoriaList(PermissionsRequiredMixin, LoginRequiredMixin, ListView):
    model = Categoria
    template_name = 'mantenedor/categoria_list.html'
    required_permissions = ('mantenedor.add_categoria',)


class CategoriaCreate(PermissionsRequiredMixin, LoginRequiredMixin, CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'mantenedor/categoria_create.html'
    success_url = reverse_lazy('mantenedor:categoria_listar')
    required_permissions = ('mantenedor.add_categoria',)


class CategoriaUpdate(PermissionsRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'mantenedor/categoria_update.html'
    success_url = reverse_lazy('mantenedor:categoria_listar')
    required_permissions = ('mantenedor.change_categoria',)


class CategoriaDelete(PermissionsRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Categoria
    template_name = 'mantenedor/categoria_delete.html'
    success_url = reverse_lazy('mantenedor:categoria_listar')
    required_permissions = ('mantenedor.delete_categoria')


def total_productos(request):

    obj = Producto.objects.filter(estado=1).order_by('-id')

    for abc in obj:
        obj_codigo = abc.codigo,
        obj_marcas = abc.marca,
        obj_descripcion = abc.descripcion,
        obj_categoria = abc.id_categoria_id

    context = {
        "obj": obj,
        "obj_codigo": obj_codigo,
        "obj_marcas": obj_marcas,
        "obj_descripcion": obj_descripcion,
        "obj_categoria": obj_categoria,

    }

    return render(request, "mantenedor/lista_productos.html", context)


def productos_disponibles(request):

    inner_qs3 = Prestamos.objects.filter(estado=1).values('id_producto_id')
    obj = Producto.objects.exclude(id__in=inner_qs3).filter(estado=1)

    for abc in obj:
        obj_codigo = abc.codigo,
        obj_marcas = abc.marca,
        obj_descripcion = abc.descripcion,
        obj_categoria = abc.id_categoria_id

    context = {

        "obj_codigo": obj_codigo,
        "obj_marcas": obj_marcas,
        "obj_descripcion": obj_descripcion,
        "obj_categoria": obj_categoria,
        "obj": obj,

    }

    return render(request, "mantenedor/total_productos.html", context)


def productos_mantencion(request):

    obj = Producto.objects.filter(estado=2)

    for abc in obj:
        obj_codigo = abc.codigo,
        obj_marcas = abc.marca,
        obj_descripcion = abc.descripcion,
        obj_categoria = abc.id_categoria_id,

    context = {
        "obj": obj,
        "obj_codigo": obj_codigo,
        "obj_marcas": obj_marcas,
        "obj_descripcion": obj_descripcion,
        "obj_categoria": obj_categoria,

    }

    return render(request, "mantenedor/productos_mantencion.html", context)


def productos_prestados(request):

    inner_qs = Prestamos.objects.filter(estado=1).values('id_producto_id')
    obj = Producto.objects.filter(id__in=inner_qs)

    for abc in obj:
        obj_codigo = abc.codigo,
        obj_marcas = abc.marca,
        obj_descripcion = abc.descripcion,
        obj_categoria = abc.id_categoria_id,

    context = {
        "obj": obj,
        "obj_codigo": obj_codigo,
        "obj_marcas": obj_marcas,
        "obj_descripcion": obj_descripcion,
        "obj_categoria": obj_categoria,

    }

    return render(request, "mantenedor/productos_prestados.html", context)


def productos_baja(request):

    obj = Producto.objects.filter(estado=0)

    for abc in obj:
        obj_codigo = abc.codigo,
        obj_marcas = abc.marca,
        obj_descripcion = abc.descripcion,
        obj_categoria = abc.id_categoria_id,

    context = {
        "obj": obj,
        "obj_codigo": obj_codigo,
        "obj_marcas": obj_marcas,
        "obj_descripcion": obj_descripcion,
        "obj_categoria": obj_categoria,

    }

    return render(request, "mantenedor/productos_baja.html", context)
