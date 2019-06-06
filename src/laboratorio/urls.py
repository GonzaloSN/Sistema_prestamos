from django.conf.urls import url
from .views import LaboratorioCreate,LaboratorioUpdate,LaboratorioView
from django.contrib.auth.mixins import LoginRequiredMixin
from laboratorio import views
from .models import Laboratorio


urlpatterns = [
    url(r'^$', LaboratorioView.as_view(), name='calendar'),
    url(r'^crear$', LaboratorioCreate.as_view(), name='laboratorio_modal'),
    url(r'^editar/(?P<pk>\d+)/$',LaboratorioUpdate.as_view(), name='laboratorio_edit_modal'),
    url(r'^dialog1$', views.reserva, name='list_reservas'),

]
