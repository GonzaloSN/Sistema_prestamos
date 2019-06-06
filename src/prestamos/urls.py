from django.conf.urls import url, include
from django.contrib import admin
from .models import *
from .views import *
from prestamos import views
#Prestamo

urlpatterns = [
    url(r'^prestamos/listar/prestamo$', PrestamoList.as_view(), name='prestamo_listar'),
    #url(r'^prestamos/crear/prestamo$', views.user, name='prestamo_crear_prestamo'),
    url(r'^prestamos/editar/prestamo/(?P<pk>\d+)/$', PrestamoUpdate.as_view(), name='prestamo_editar'),
    url(r'^prestamos/eliminar/prestamo/(?P<pk>\d+)/$', PrestamoDelete.as_view(), name='prestamo_eliminar'),
    url(r'^prestamos/crear/prestamos$', PrestamoCreate.as_view(), name='prestamo_crear'),
    url(r'^prestamos/devolucion/(?P<pk>\d+)/$', Devolucion.as_view(), name='devolucion'),
    url(r'^prestamos/listar/devoluciones$', DevolucionList.as_view(), name='devolucion_listar'),
    url(r'^prestamos/listar/retrasos$', RetrasosList.as_view(), name='retrasos'),
    url(r'^prestamos/listar/danos$', DanosList.as_view(), name='danos'),

    url(r'^prestamos/listar/prestamo/dialog1$', views.prestamo_activo, name='list_prestamos'),
    url(r'^prestamos/listar/prestamo/dialog2$', views.prestamo_atrasado, name='list_prestamos_atrasados'),
]