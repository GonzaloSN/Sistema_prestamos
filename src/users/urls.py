from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^registrar', views.UserCreateView.as_view(), name="registrar"),
    url(r'^editar/(?P<pk>[0-9]+)/$', views.UserUpdateView.as_view(), name='editar'),
    url(r'^eliminar/(?P<pk>\d+)/$', views.UserDeleteView.as_view(), name="eliminar"),
    url(r'^$', views.UserListView.as_view(), name='listar'),

    #url(r'^account/', views.UserAccountView.as_view(), name='account'),

    
]
