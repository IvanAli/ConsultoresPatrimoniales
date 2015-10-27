from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.loginView, name='login'),
    url(r'^authentication$', views.loginAuthentication, name='loginAuthentication'),
    url(r'^home/$', views.home, name='home'),
    url(r'^nuevoCliente/$', views.nuevoClienteView, name='nuevoCliente'),
    url(r'^authenticationC$', views.nuevoClienteAuth, name='nuevoClienteAuth'),
    url(r'^clientes/$', views.clientesView, name='clientes'),
    url(r'^clientes/(?P<idCliente>[0-9]+)/$', views.infoClienteView, name='infoCliente'),
    url(r'^preNuevaComparativa/$', views.preNuevaComparativaView, name='preNuevaComparativa'),
    url(r'^nuevaComparativa/(?P<idCliente>[0-9]+)/$', views.nuevaComparativaView, name='nuevaComparativa'),
    url(r'^nuevaComparativaAuth/(?P<idCliente>[0-9]+)/$', views.nuevaComparativaAuth, name='nuevaComparativaAuth'),
    url(r'^comparativas/$', views.comparativasView, name='comparativas'),
    url(r'^polizas/$', views.polizasView, name='polizas'),
]