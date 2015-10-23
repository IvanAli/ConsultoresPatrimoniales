from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.loginView, name='login'),
    url(r'^authentication$', views.loginAuthentication, name='loginAuthentication'),
    url(r'^home/$', views.home, name='home'),
    url(r'^clientes/$', views.clientesView, name='clientes'),
]
