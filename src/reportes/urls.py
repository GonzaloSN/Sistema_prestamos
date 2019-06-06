from django.conf.urls import url, include
from django.contrib import admin
from .views import *
from reportes import views


urlpatterns = [
    url(r'^$', HomeView.as_view(), name='hom'),
    url(r'^report$', Reporte.as_view(), name='report'),
    url(r'^report/activo$', ReporteActivo.as_view(), name='report_activo'),
    url(r'^api/data/', get_data, name='api-data'),
    url(r'^api/chart/data/', ChartData.as_view()),
    #url(r'^reportes/pdf$', views.report_pdf, name='pdf'),
]