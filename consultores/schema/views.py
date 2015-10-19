from django.shortcuts import render
from . import forms
from .models import Agente
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.

def login(request):
    return render(request, "schema/login.html", {})

def loginAuthentication(request):
    if request.method == "POST":
        login_form = forms.LoginForm(request.POST)
        if login_form.is_valid():
            user_form = login_form.cleaned_data['user']
            password_form = login_form.cleaned_data['password']
            user_db = Agente.objects.get(usuario=user_form)
            if user_db.contrasena == password_form:
                request.session['user'] = user_db.idUsuario
                return HttpResponseRedirect(reverse('schema:home'))
            else:
                context = {'error_wrongpassword': "Contraseña incorrecta"}
                return render(request, 'schema/login.html', context)
        else:
            context = {'error_missingfields': "Campos sin llenar"}
            return render(request, 'schema/login.html', context)


def home(request):
    context = {'user': Agente.objects.get(idUsuario=request.session['user'])}
    return render(request, "schema/home.html", context)
