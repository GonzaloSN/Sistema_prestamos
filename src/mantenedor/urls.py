from django.conf.urls import url, include
from django.contrib import admin
from .models import *
from .views import *
from .models import *
from mantenedor import views


urlpatterns = [
    #producto
    url(r'^mantenedor/listar/producto$', ProductoList.as_view(), name='producto_listar'),
    url(r'^mantenedor/crear/producto$', ProductoCreate.as_view(), name='producto_crear'),
    url(r'^mantenedor/editar/producto/(?P<pk>\d+)/$', ProductoUpdate.as_view(), name='producto_editar'),
    url(r'^mantenedor/eliminar/producto_estado/(?P<pk>\d+)/$', ProductoEstado.as_view(), name='producto_estado'),
    url(r'^mantenedor/listar/producto/baja$', ProductoDeBajaList.as_view(), name='producto_listar_baja'),
    url(r'^mantenedor/listar/producto/mantencion$', ProductoMantencionList.as_view(), name='producto_listar_mantencion'),
    #url(r'^mantenedor/eliminar/producto/(?P<pk>\d+)/$', ProductoDelete.as_view(), name='producto_eliminar'),
    #categoria
    url(r'^mantenedor/listar/categoria$', CategoriaList.as_view(), name='categoria_listar'),
    url(r'^mantenedor/crear/categoria$', CategoriaCreate.as_view(), name='categoria_crear'),
    url(r'^mantenedor/editar/categoria/(?P<pk>\d+)/$', CategoriaUpdate.as_view(), name='categoria_editar'),
    url(r'^mantenedor/eliminar/categoria/(?P<pk>\d+)/$', CategoriaDelete.as_view(), name='categoria_eliminar'),
    #BootstrapDialog
    url(r'^mantenedor/listar/producto/dialog$', views.total_productos, name='producto_listar_dialog'),
    url(r'^mantenedor/listar/producto/dialog2$', views.productos_disponibles, name='producto_listar_dialog2'),
    url(r'^mantenedor/listar/producto/dialog3$', views.productos_mantencion, name='producto_listar_dialog3'),
    url(r'^mantenedor/listar/producto/dialog4$', views.productos_prestados, name='producto_listar_dialog4'),
    url(r'^mantenedor/listar/producto/dialog5$', views.productos_baja, name='producto_listar_dialog5'),
]