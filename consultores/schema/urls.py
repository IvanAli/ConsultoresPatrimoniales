from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.loginView, name='login'),
    url(r'^logout/$', views.logoutView, name='logout'),
    url(r'^authentication/$', views.loginAuthentication, name='loginAuthentication'),
    url(r'^home/$', views.home, name='home'),
    url(r'^nuevoCliente/$', views.nuevoClienteView, name='nuevoCliente'),
    url(r'^authenticationC/$', views.nuevoClienteAuth, name='nuevoClienteAuth'),
    url(r'^clientes/$', views.clientesView, name='clientes'),
    url(r'^clientes/(?P<idCliente>[0-9]+)/$', views.infoClienteView, name='infoCliente'),
    url(r'^seleccionCliente/(?P<context_type>[a-zA-Z]+)/$', views.seleccionClienteView, name='seleccionCliente'),
    url(r'^seleccionOrdenServicio/$', views.seleccionOrdenServicioView, name='seleccionOrdenServicio'),
    url(r'^nuevaComparativa/(?P<idCliente>[0-9]+)/$', views.nuevaComparativaView, name='nuevaComparativa'),
    url(r'^enviarCotizacionTramites/(?P<idComparativa>[0-9]+)/$', views.enviarCotizacionTramitesView, name='enviarCotizacionTramites'),
    url(r'^nuevaPoliza/(?P<idOrdenServicio>[0-9]+)/$', views.nuevaPolizaView, name='nuevaPoliza'),
    url(r'^nuevoPago/(?P<idPoliza>[0-9]+)/$', views.nuevoPagoView, name='nuevoPago'),
    url(r'^nuevoPagoAuth/(?P<idPoliza>[0-9]+)/$', views.nuevoPagoAuthView, name='nuevoPagoAuth'),
    url(r'^nuevaPolizaAuth/(?P<idOrdenServicio>[0-9]+)/$', views.nuevaPolizaAuthView, name='nuevaPolizaAuth'),
    url(r'^nuevaCotizacion/(?P<idComparativa>[0-9]+)/$', views.nuevaCotizacionView, name='nuevaCotizacion'),
    url(r'^nuevaComparativaAuth/(?P<idCliente>[0-9]+)/$', views.nuevaComparativaAuth, name='nuevaComparativaAuth'),
    url(r'^nuevaComparativaAPAuth/(?P<idCliente>[0-9]+)/$', views.nuevaComparativaAPAuth, name='nuevaComparativaAPAuth'),
    url(r'^nuevaCotizacionAuth/(?P<idComparativa>[0-9]+)/$', views.nuevaCotizacionAuth, name='nuevaCotizacionAuth'),
    url(r'^comparativas/$', views.comparativasView, name='comparativas'),
    url(r'^comparativas/(?P<idComparativa>[0-9]+)/$', views.comparativaClienteView, name='comparativaCliente'),
    url(r'^polizas/$', views.polizasView, name='polizas'),
    url(r'^polizas/(?P<idPoliza>[0-9]+)/$', views.polizaClienteView, name='polizaCliente'),
    url(r'^nuevoClienteAuth/$', views.nuevoClienteAuth, name='nuevoClienteAuthentication'),
    url(r'^cotizaciones/(?P<idCotizacion>[0-9]+)/$', views.cotizacionClienteView, name='cotizacionCliente'),
    # url(r'^comparativa.pdf$', views.ComparativaPDFView.as_view(), name='comparativapdf'),
    url(r'^enviarComparativa/(?P<idComparativa>[0-9]+)/$', views.enviarComparativaView, name='enviarComparativa'),
    url(r'^marcarConcluida/(?P<idComparativa>[0-9]+)/$', views.marcarComparativaConcluidaView, name='marcarConcluida'),
    url(r'^marcarPreferida/(?P<idCotizacion>[0-9]+)/$', views.marcarCotizacionPreferidaView, name='marcarCotizacionPreferida'),
    # url(r'^comparativa.pdf$', views.ComparativaPDFView.as_view(), name='comparativapdf'),
    url(r'^agentes/$', views.agentesView, name='agentes'),
    url(r'^aseguradoras/$', views.aseguradorasView, name='aseguradoras'),
    url(r'^seguros/$', views.segurosView, name='seguros'),
]
