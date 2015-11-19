from django.shortcuts import render
from . import forms
from django.forms import formset_factory
from .models import Agente, Cliente, ClienteFisico, ClienteMoral, Seguro, TipoSeguro, OrdenServicio, Comparativa, Aseguradora, Cobertura, Cotizacion, CoberturaUtilizada
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from easy_pdf.views import PDFTemplateView
from . import managers
# Create your views here.

"""
    AGREGAR DECORATORS - PENDIENTE
    PS: Me gusta codear en ingles
"""

# HELPER FUNCTIONS
def getUser(username):
    try:
        user = User.objects.get(username=username)
        return user
    except User.DoesNotExist:
        return None

def isAgente(user):
    return user.groups.filter(name='agente').exists()

# VIEWS
def loginView(request):
    return render(request, "schema/login.html", {})

def loginAuthentication(request):
    if request.method == "POST":
        login_form = forms.LoginForm(request.POST)
        if login_form.is_valid():
            user_form = login_form.cleaned_data['user']
            password_form = login_form.cleaned_data['password']
            user = authenticate(username=user_form, password=password_form)
            if user is not None:
                if user.is_active:
                    # request.session['username'] = user.username
                    login(request, user)
                    return HttpResponseRedirect(reverse('schema:home'))
                else:
                    context = {'error_sessionexpired': 'Sesión expirada'}
                    return render(request, 'schema/login.html', context)
            else:
                context = {'error_wrongpassword': "Contraseña incorrecta"}
                return render(request, 'schema/login.html', context)
        else:
            context = {'error_missingfields': "Campos sin llenar"}
            return render(request, 'schema/login.html', context)

def registerAgente(request):
    return HttpResponse("Work in Progress")

def home(request):
    if isAgente(request.user):
        context = {'agente': Agente.objects.get(userAgente=request.user)}
        return render(request, 'schema/home.html', context)
    else:
        print("NOT AN AGENT")

def nuevoClienteView(request):
    context = {'cliente': request.user.agente.clientes}
    return render(request, "schema/nuevoCliente.html", context)

def nuevoClienteAuth(request):
    if request.method == "POST":
        datos_form = forms.nuevoClienteForm(request.POST)
        if datos_form.is_valid():
            cliente = datos_form.save()
            request.user.agente.clientes.add(cliente)
            return HttpResponseRedirect(reverse('schema:clientes'))
        else:
            context = {'error_missingfields': "Campos sin llenar"}
            return render(request, 'schema/nuevoCliente.html', context)

def clientesView(request):
    context = {'clientes': request.user.agente.clientes}
    return render(request, 'schema/clientes.html', context)

def infoClienteView(request, idCliente):
    context = {'cliente': Cliente.objects.get(pk=idCliente)}
    return render(request, 'schema/infocliente.html', context)

def preNuevaComparativaView(request):
    context = {'clientes': request.user.agente.clientes}
    return render(request, 'schema/preNuevaComparativa.html', context)

def nuevaComparativaView(request, idCliente):
    context = {
        'cliente': request.user.agente.clientes.get(pk=idCliente),
        'seguros': Seguro.objects.all(),
        'APform': forms.SeguroAPForm(),
        'Cform': forms.SeguroCForm(),
        'Rform': forms.SeguroRForm(),
        'Gform': forms.SeguroGForm(),
        'Vform': forms.SeguroVForm(),
        'Hform': forms.SeguroHForm(),
        'Iform': forms.SeguroIForm(),
        'Eform': forms.SeguroEForm(),
        'ECform': forms.SeguroECForm(),
        'coberturas': Cobertura.objects.all(),
        'coberturasAP': Cobertura.objects.filter(seguro__pk='AP'),
        'coberturasC': Cobertura.objects.filter(seguro__pk='C'),
        'coberturasR': Cobertura.objects.filter(seguro__pk='R'),
        'coberturasG': Cobertura.objects.filter(seguro__pk='G'),
        'coberturasV': Cobertura.objects.filter(seguro__pk='V'),
        'coberturasV': Cobertura.objects.filter(seguro__pk='V'),
        'coberturasV': Cobertura.objects.filter(seguro__pk='V'),
        'coberturasE': Cobertura.objects.filter(seguro__pk='E'),
        'coberturasEC': Cobertura.objects.filter(seguro__pk='EC'),
    }
    return render(request, 'schema/nuevaComparativa.html', context)

def nuevaComparativaAuth(request, idCliente):
    if request.method == "POST":
        if request.POST['tipo'] == 'NULL':
            return HttpResponse('Tipo de seguro no seleccionado')

        if request.POST['tipo'] == 'AP':
            APform = forms.SeguroAPForm(request.POST)
            if APform.is_valid():
                seguroComparativa = APform.save()
                seguroComparativa.nombre = Seguro.objects.get(pk='AP')
                seguroComparativa.save()
                comparativa = Comparativa(tipoSeguro=seguroComparativa)
                # comparativa.tipoSeguro.nombre = Seguro.objects.get(pk='AP')
                # seguroNombre = Seguro.objects.get(pk='AP')
                # comparativa.tipoSeguro = TipoSeguro(nombre=seguroNombre)
                # comparativa.tipoSeguro.save()
                comparativa.save()

                checklist = request.POST.getlist('coberturaAP')
                for checked in checklist:
                    print("id cobertura:", checked)
                    comparativa.coberturas.add(Cobertura.objects.get(pk=checked))
                ordenServicio = OrdenServicio(cliente=Cliente.objects.get(pk=idCliente),comparativa=comparativa)
                ordenServicio.save()
                return HttpResponseRedirect(reverse('schema:comparativas'))
            else:
                for err in APform.errors:
                    print("error:")
                    print(err)
                return HttpResponse('Error de datos')
        if request.POST['tipo'] == 'C':
            Cform = forms.SeguroCForm(request.POST)
            if Cform.is_valid():
                seguroComparativa = Cform.save()
                comparativa = Comparativa(tipoSeguro=seguroComparativa)
                comparativa.save()
                ordenServicio = OrdenServicio(cliente=Cliente.objects.get(pk=idCliente),comparativa=comparativa)
                ordenServicio.save()
                return HttpResponseRedirect(reverse('schema:comparativas'))
            else:
                return HttpResponse("Forma invalida")
        if request.POST['tipo'] == 'R':
            Rform = forms.SeguroRForm(request.POST)
            if Rform.is_valid():
                seguroComparativa = Rform.save()
                comparativa = Comparativa(tipoSeguro=seguroComparativa)
                comparativa.save()
                ordenServicio = OrdenServicio(cliente=Cliente.objects.get(pk=idCliente),comparativa=comparativa)
                ordenServicio.save()
                return HttpResponseRedirect(reverse('schema:comparativas'))
            else:
                return HttpResponse("Forma invalida")
        if request.POST['tipo'] == 'G':
            print("Nombre", request.POST['nombreAsegurado'])
            print("Coaseguro", request.POST['coaseguro'])
            print("Topecoaseguro", request.POST['topeCoaseguro'])
            Gform = forms.SeguroGForm(request.POST)
            if Gform.is_valid():
                seguroComparativa = Gform.save()
                comparativa = Comparativa(tipoSeguro=seguroComparativa)
                comparativa.save()
                ordenServicio = OrdenServicio(cliente=Cliente.objects.get(pk=idCliente),comparativa=comparativa)
                ordenServicio.save()
                return HttpResponseRedirect(reverse('schema:comparativas'))
            else:
                for err in Gform.errors:
                    print("error:")
                    print(err)
                return HttpResponse("Forma invalida")
        if request.POST['tipo'] == 'V':
            Vform = forms.SeguroVForm(request.POST)
            if Vform.is_valid():
                seguroComparativa = Vform.save()
                comparativa = Comparativa(tipoSeguro=seguroComparativa)
                comparativa.save()
                ordenServicio = OrdenServicio(cliente=Cliente.objects.get(pk=idCliente),comparativa=comparativa)
                ordenServicio.save()
                return HttpResponseRedirect(reverse('schema:comparativas'))
            else:
                return HttpResponse("Forma invalida")
        if request.POST['tipo'] == 'H':
            Hform = forms.SeguroHForm(request.POST)
            if Hform.is_valid():
                seguroComparativa = Hform.save()
                comparativa = Comparativa(tipoSeguro=seguroComparativa)
                comparativa.save()
                ordenServicio = OrdenServicio(cliente=Cliente.objects.get(pk=idCliente),comparativa=comparativa)
                ordenServicio.save()
                return HttpResponseRedirect(reverse('schema:comparativas'))
            else:
                return HttpResponse("Forma invalida")
        if request.POST['tipo'] == 'I':
            Iform = forms.SeguroIForm(request.POST)
            if Iform.is_valid():
                seguroComparativa = Iform.save()
                comparativa = Comparativa(tipoSeguro=seguroComparativa)
                comparativa.save()
                ordenServicio = OrdenServicio(cliente=Cliente.objects.get(pk=idCliente),comparativa=comparativa)
                ordenServicio.save()
                return HttpResponseRedirect(reverse('schema:comparativas'))
            else:
                return HttpResponse("Forma invalida")
    # tmp
    return HttpResponse('Autenticando nueva Comparativa...')


def comparativasView(request):
    context = {'clientes': request.user.agente.clientes}
    return render(request, 'schema/comparativas.html', context)

def comparativaClienteView(request, idComparativa):
    context = {'comparativa': Comparativa.objects.get(pk=idComparativa)}
    return render(request, 'schema/comparativacliente.html', context)

def cotizacionClienteView(request, idCotizacion):
    context = {'cotizacion': Cotizacion.objects.get(pk=idCotizacion)}
    return render(request, 'schema/cotizacioncliente.html', context)

def nuevaCotizacionView(request, idComparativa):
    comparativa = Comparativa.objects.get(pk=idComparativa)
    tipo = comparativa.tipoSeguro.nombre.idSeguro
    coberturaUtilizadaForm = forms.CoberturaUtilizadaForm()
    coberturaUtilizadaForm.fields['idCobertura'].queryset = Cobertura.objects.filter(seguro__pk=tipo)
    context = {
        'comparativa': Comparativa.objects.get(pk=idComparativa),
        'aseguradoras': Aseguradora.objects.all(),
        'cotizacionForm': forms.CotizacionForm(),
        'coberturaUtilizadaForm': coberturaUtilizadaForm,
        'coberturas': Cobertura.objects.filter(seguro__pk=tipo),
    }
    return render(request, 'schema/nuevaCotizacion.html', context)

# VALIDACION DE COBERTURAS INTRODUCIDAS PENDIENTES
def nuevaCotizacionAuth(request, idComparativa):
    cotizacionForm = forms.CotizacionForm(request.POST, instance=Cotizacion())
    cuForms = [forms.CoberturaUtilizadaForm(request.POST, prefix=str(x), instance=CoberturaUtilizada()) for x in range(0, 3)]
    if cotizacionForm.is_valid() and any([coberturaForm.is_valid() for coberturaForm in cuForms]):
        cotizacion = cotizacionForm.save()
        for coberturaForm in cuForms:
            print(coberturaForm)
            newCobertura = coberturaForm.save(commit=False)
            newCobertura.cotizacion = cotizacion
            newCobertura.save()
        cotizacion.comparativa = Comparativa.objects.get(pk=idComparativa)
        cotizacion.save()
        return HttpResponseRedirect(reverse('schema:comparativas'))
    else:
        for err in cotizacionForm.errors:
            print("error:", err)
        for element in cuForms:
            for err in element.errors:
                print("error cobertura:", err)
    return HttpResponse("error")

def polizasView(request):
    context = {'clientes': request.user.agente.clientes}
    return render(request, 'schema/polizas.html', context)

class ComparativaPDFView(PDFTemplateView):
    template_name = "schema/pdf/comparativapdf.html"

    def get_context_data(self, **kwargs):
        return super(ComparativaPDFView, self).get_context_data(
            pagesize="A4",
            title="Comparativa",
            **kwargs
        )
