from django.shortcuts import render
from . import forms
from .models import Agente, Cliente, ClienteFisico, ClienteMoral, TipoSeguro
from django.http import HttpResponseRedirect
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

# helper functions
def getUser(username):
    try:
        user = User.objects.get(username=username)
        return user
    except User.DoesNotExist:
        return None

def isAgente(user):
    return user.groups.filter(name='agente').exists()

# views

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

def clientesView(request):
    context = {'clientesFisicos': request.user.agente.clientes}
    return render(request, 'schema/clientes.html', context)

def comparativasView(request):
    context = {'ordenes': request.user.agente.ordenservicio_set}
    return render(request, 'schema/comparativas.html', context)

def polizasView(request):
    context = {'ordenes': request.user.agente.ordenservicio_set}
    return render(request, 'schema/polizas.html', context)

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

def nuevaComparativaAuthView(request, idCliente):
    if request.method == "POST":
        nuevaComparativaForm = forms.SeguroAPForm(request.POST)
        if nuevaComparativaForm.is_valid():
            nuevaComparativaForm.save()
            return HttpResponseRedirect('http://www.google.com/')
            # request.user.agente.ordenservicio_set.get(cliente__idCliente=idCliente).comparativa = nuevaComparativaForm
        else:
            return HttpResponse('Error de datos')
    return HttpResponse('Autenticando nueva Comparativa...')

def nuevoCliente(request):
    context = {'cliente': request.user.agente.cliente_set}
    return render(request, "schema/nuevoCliente.html", context)

def nuevoClienteAuthentication(request):
    if request.method == "POST":
        datos_form = forms.nuevoClienteForm(request.POST)
        if datos_form.is_valid():
            datos_form.save()
            return HttpResponseRedirect(reverse('schema:login'))
        else:
            context = {'error_missingfields': "Campos sin llenar"}
            return render(request, 'schema/nuevoCliente.html', context)
