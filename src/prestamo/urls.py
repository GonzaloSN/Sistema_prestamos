"""sisfores URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete

urlpatterns = [
    #modelwidget
    url(r'^select2/', include('django_select2.urls')),

    url(r'^admin/', admin.site.urls),
    url(r'^usuario/', include('users.urls', namespace='usuario')),

    #URL de mantenedor

    url(r'^', include('mantenedor.urls', namespace="mantenedor")),

    #Url de Prestamos

    url(r'^', include('prestamos.urls', namespace="prestamos")),

    #Url de Laboratorio

    url(r'^laboratorio/', include('laboratorio.urls', namespace="laboratorio")),

    #Url de Reportes

    url(r'^reportes/', include('reportes.urls', namespace="reportes")),

    # URL del Home

    url(r'^', include('home.urls', namespace='home')),

    # URL Cuentas de usuario

    url(r'^accounts/', include('allauth.urls')),

    # urls de login y de recuperacion de contraseña

    url(r'^password/reset/', password_reset,
        {'template_name': 'account/password_reset_email_form.html',
         'email_template_name': 'account/password_reset_email.html'},
        name='password_reset'),

    url(r'^password/reset-done', password_reset_done,
        {'template_name': 'account/password_reset_email_done.html'},
        name='password_reset_done'),

    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', password_reset_confirm,
        {'template_name': 'account/password_reset_email_confirm.html'},
        name='password_reset_confirm'),

    url(r'^reset/done', password_reset_complete,
        {'template_name': 'account/password_reset_email_complete.html'},
        name='password_reset_complete'),

]
