from django.shortcuts import render
from . import forms
from django.forms import formset_factory
from .models import Agente, Administrador, Cliente, ClienteFisico, ClienteMoral, TipoSeguro, OrdenServicio, Comparativa, Aseguradora, Cobertura
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
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

def whichUser(user):
    groupID = 0;
    if user.groups.filter(name="admin").exists():
        groupID = 2
    elif user.groups.filter(name='agente').exists():
        groupID = 1
    return groupID

# VIEWS
@csrf_protect
def loginView(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('schema:home'))
    else:
        context = {}
        return render(request, "schema/login.html", context)    

@csrf_protect
def logoutView(request):
    logout(request)
    context = {'message_logoutsuccess': "¡Has salido exitosamente!"}
    return render(request, "schema/login.html", context)

@csrf_protect
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
                context = {'error_wrongpassword': "Usuario o contraseña incorrectos"}
                return render(request, 'schema/login.html', context)
        else:
            context = {'error_missingfields': "Campos sin llenar"}
            return render(request, 'schema/login.html', context)

def registerAgente(request):
    return HttpResponse("Work in Progress")

@login_required(redirect_field_name='')
def home(request):
    if whichUser(request.user) == 1:
        context = {'agente': Agente.objects.get(userAgente=request.user)}
        return render(request, 'schema/home.html', context)
    elif whichUser(request.user) == 2:
        context = {'agente': Administrador.objects.get(userAdmin=request.user)}
        return render(request, 'schema/homeAdmin.html', context)        

@login_required(redirect_field_name='')
def nuevoClienteView(request):
    context = {'cliente': request.user.agente.clientes}
    return render(request, "schema/nuevoCliente.html", context)

@login_required(redirect_field_name='')
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

@login_required(redirect_field_name='')
def clientesView(request):
    context = {'clientes': request.user.agente.clientes}
    return render(request, 'schema/clientes.html', context)

@login_required(redirect_field_name='')
def infoClienteView(request, idCliente):
    context = {'cliente': Cliente.objects.get(pk=idCliente)}
    return render(request, 'schema/infocliente.html', context)

@login_required(redirect_field_name='')
def preNuevaComparativaView(request):
    context = {'clientes': request.user.agente.clientes}
    return render(request, 'schema/preNuevaComparativa.html', context)

@login_required(redirect_field_name='')
def nuevaComparativaView(request, idCliente):
    context = {
        'cliente': request.user.agente.clientes.get(pk=idCliente),
        'seguros': TipoSeguro.objects,
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
    }
    return render(request, 'schema/nuevaComparativa.html', context)

@login_required(redirect_field_name='')
def nuevaComparativaAuth(request, idCliente):
    if request.method == "POST":
        """
        for key in request.POST:
            print(request.POST[key])
        """
        if request.POST['tipo'] == 'NULL':
            return HttpResponse('Tipo de seguro no seleccionado')

        if request.POST['tipo'] == 'AP':
            APform = forms.SeguroAPForm(request.POST)
            if APform.is_valid():
                seguroComparativa = APform.save()
                comparativa = Comparativa(tipoSeguro=seguroComparativa)
                comparativa.tipoSeguro.tipo = 'AP'
                comparativa.save()

                checklist = request.POST.getlist('coberturaAP')
                for checked in checklist:
                    print("id cobertura:", checked)
                    comparativa.coberturas.add(Cobertura.objects.get(pk=checked))
                # Comparativa.objects.order_by('-pk')[0].tipoSeguro_id = 'AP'
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

@login_required(redirect_field_name='')
def comparativasView(request):
    context = {'clientes': request.user.agente.clientes}
    return render(request, 'schema/comparativas.html', context)

@login_required(redirect_field_name='')
def comparativaClienteView(request, idComparativa):
    context = {'comparativa': Comparativa.objects.get(pk=idComparativa)}
    return render(request, 'schema/comparativacliente.html', context)

@login_required(redirect_field_name='')
def nuevaCotizacionView(request, idComparativa):
    context = {
        'comparativa': Comparativa.objects.get(pk=idComparativa),
        'aseguradoras': Aseguradora.objects.all(),
        'cotizacionForm': forms.CotizacionForm(),
        'coberturaUtilizadaForm': forms.CoberturaUtilizadaForm(),
        'coberturas': Cobertura.objects.all(),
    }
    return render(request, 'schema/nuevaCotizacion.html', context)

# VALIDACION DE COBERTURAS INTRODUCIDAS PENDIENTES
@login_required(redirect_field_name='')
def nuevaCotizacionAuth(request, idComparativa):
    cotizacionForm = forms.CotizacionForm(request.POST)
    if cotizacionForm.is_valid():
        cotizacion = cotizacionForm.save()
        cotizacion.comparativa = Comparativa.objects.get(pk=idComparativa)
        cotizacion.save()
        return HttpResponseRedirect(reverse('schema:comparativas'))
    else:
        for err in cotizacionForm.errors:
            print("error:", err)

@login_required(redirect_field_name='')
def polizasView(request):
    context = {'clientes': request.user.agente.clientes}
    return render(request, 'schema/polizas.html', context)
