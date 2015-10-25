from django import forms
from django.forms import ModelForm
from .models import Agente, Cliente

class LoginForm(forms.Form):
    user = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30)

class nuevoClienteForm(forms.ModelForm):
	class Meta:
 		model = Cliente
 		fields= ['nombre','apellidoPaterno','apellidoMaterno','email','telefonoLada','telefono','edad','sexo','rfc','calle','numeroExt',
 		'numeroInt','colonia','ciudad','estado','codigoPostal']

   