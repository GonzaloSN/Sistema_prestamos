from django.contrib.auth.mixins import LoginRequiredMixin
from users.mixins import PermissionsRequiredMixin
from django.views.generic import TemplateView, ListView
from django.shortcuts import render
from mantenedor.models import Producto, Categoria
from prestamos.models import Prestamos
from laboratorio.models import Laboratorio
from datetime import datetime
from django.db.models import Avg, Max, Min, Sum, Count
from django.contrib.auth.models import User


class HomeTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'home/index.html'


def dashboard(request):
    obj1 = Producto.objects.filter(estado=1).count()
    obj2 = Prestamos.objects.filter(estado=1).count()
    obj3 = Laboratorio.objects.count()
    obj4 = Prestamos.objects.filter(fecha_devolucion__lte=datetime.now(), estado=1).count()

    inner_qs2 = Prestamos.objects.filter(estado=1).values('id_producto_id')
    obj5 = Producto.objects.exclude(id__in=inner_qs2).filter(estado=1).count()

    obj6 = Producto.objects.filter(estado=2).count()
    obj7 = Producto.objects.filter(estado=0).count()

    inner_qs = Prestamos.objects.filter(estado=1).values('id_producto_id')
    obj8 = Producto.objects.filter(id__in=inner_qs).count()

    obj9 = User.objects.all().count()

    # var1 = Prestamos.objects.values('id_producto_id__codigo')
    # v = var1.annotate(max=Count('id_producto_id'))
    # inner = v.latest('max')

    # var = Prestamos.objects.values('id_producto_id__codigo')
    # contador = var.annotate(total=Count('id_producto_id__codigo'))
    # inner = contador.latest('total')

    # inner = v.latest('max')

    context = {
        "obj1_1": obj1,
        "obj2": obj2,
        "obj3": obj3,
        "obj4": obj4,
        "obj5": obj5,
        "obj6": obj6,
        "obj7": obj7,
        "obj8": obj8,
        "obj9": obj9,
    }

    return render(request, "home/dashboard.html", context)


def usuarios(request):

    obj = User.objects.all().order_by('-id')

    for abc in obj:
        obj_username = abc.username,
        obj_nombre = abc.first_name,
        obj_apellido = abc.last_name,
        obj_email = abc.email,

    context = {
        "obj": obj,
        "obj_username": obj_username,
        "obj_nombre": obj_nombre,
        "obj_apellido": obj_apellido,
        "obj_email": obj_email,
    }

    return render(request, "home/list_user.html", context)

