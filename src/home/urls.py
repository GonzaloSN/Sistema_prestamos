from django.conf.urls import url
from .views import HomeTemplateView, dashboard, usuarios

# urlpatterns = [
#     url(r'^$', views.Dashboard, name='index'),
#     #url(r'^$', HomeTemplateView.as_view(), name='index'),
# ]

urlpatterns = [
    url(r'^$', HomeTemplateView.as_view(), name='index'),
    url(r'^dashboard$', dashboard, name='dashboard'),
    url(r'^usuarios$', usuarios, name='usuarios'),

]
