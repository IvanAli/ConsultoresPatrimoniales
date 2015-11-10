from django.shortcuts import render
from . import forms
from .models import Agente, Cliente, ClienteFisico, ClienteMoral, TipoSeguro, OrdenServicio, Comparativa
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
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
    APform = forms.SeguroAPForm()
    context = {
        'cliente': request.user.agente.clientes.get(pk=idCliente),
        'seguros': TipoSeguro.objects,
        'APform': APform}
    return render(request, 'schema/nuevaComparativa.html', context)

def nuevaComparativaAuth(request, idCliente):
    if request.method == "POST":
        """
        tipoSeguro = request.POST['tipoSeguro']
        if tipoSeguro == 'None':
            return render(request, 'schema/nuevaComparativa.html', {})
        if tipoSeguro == 'AP':
        """
        if request.POST['idTipoSeguro'] == 'NULL':
            return HttpResponse('Tipo de seguro no seleccionado')
        if request.POST['idTipoSeguro'] == 'AP':
            seguroAPf = forms.SeguroAPForm(request.POST)
            if seguroAPf.is_valid():
                seguroComparativa = seguroAPf.save()
                comparativa = Comparativa(tipoSeguro=seguroComparativa)
                comparativa.save()
                Comparativa.objects.order_by('-pk')[0].tipoSeguro_id = 'AP'
                ordenServicio = OrdenServicio(cliente=Cliente.objects.get(pk=idCliente),comparativa=comparativa)
                ordenServicio.save()
                return HttpResponseRedirect(reverse('schema:comparativas'))
            else:
                for err in nuevaComparativaForm.errors:
                    print("error:")
                    print(err)
                return HttpResponse('Error de datos')
        if request.POST['idTipoSeguro'] == 'C':
            return HttpResponse('C')
        if request.POST['idTipoSeguro'] == 'R':
            return HttpResponse('R')
        if request.POST['idTipoSeguro'] == 'G':
            return HttpResponse('G')

    # tmp
    return HttpResponse('Autenticando nueva Comparativa...')


def comparativasView(request):
    context = {'clientes': request.user.agente.clientes}
    return render(request, 'schema/comparativas.html', context)

def polizasView(request):
    context = {'clientes': request.user.agente.clientes}
    return render(request, 'schema/polizas.html', context)
