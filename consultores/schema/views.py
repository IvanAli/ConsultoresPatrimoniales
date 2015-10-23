from django.shortcuts import render
from . import forms
from .models import Agente, Cliente, ClienteFisico, ClienteMoral
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
