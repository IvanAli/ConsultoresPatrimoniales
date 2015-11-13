from django import forms
from django.forms import ModelForm
from .models import Agente, Cliente, SeguroAP

class LoginForm(forms.Form):
    user = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30)

class nuevoClienteForm(forms.ModelForm):
	
	class Meta:
 		model = Cliente
 		fields= ['nombre','apellidoPaterno','apellidoMaterno','email','telefonoLada','telefono','edad','sexo','rfc','calle','numeroExt',
 		'numeroInt','colonia','ciudad','estado','codigoPostal','calleFact','numeroExtFact','numeroIntFact','coloniaFact','ciudadFact'
 		,'estadoFact','codigoPostalFact']

 		def clean_email(self):
 			email = self.cleaned_data.get('email')
 			provider = email.split("@")
 			extension = provider.split('.')

 			if not extension == "edu" :
 				raise forms.ValidationError("lalalala")
 			return email

class SeguroAPForm(forms.ModelForm):
	class Meta:
		model = SeguroAP
		fields = ['marca', 'modelo', 'ano', 'descripcion', 'pasajeros', 'estadoCirculacion']
        # fields = ['idTipoSeguro', 'marca', 'modelo', 'ano', 'descripcion', 'pasajeros', 'estadoCirculacion']

# class SeguroCForm(forms.Form):
# 	class Meta:
# 		model = SeguroC
# 		fields = ['marca', 'modelo', 'ano', 'descripcion', 'pasajeros', 'estadoCirculacion']

# class SeguroRForm(forms.Form):
# 	class Meta:
# 		model = SeguroR
# 		fields = ['marca', 'modelo', 'ano', 'descripcion', 'pasajeros', 'estadoCirculacion']
