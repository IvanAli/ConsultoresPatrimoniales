from django import forms
from django.forms import ModelForm
from .models import Agente, SeguroAP

class LoginForm(forms.Form):
    user = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30)

class SeguroAPForm(forms.ModelForm):
	class Meta:
		model = SeguroAP
		fields = ['marca', 'modelo', 'ano', 'descripcion', 'pasajeros', 'estadoCirculacion']

# class SeguroCForm(forms.Form):
# 	class Meta:
# 		model = SeguroC
# 		fields = ['marca', 'modelo', 'ano', 'descripcion', 'pasajeros', 'estadoCirculacion']

# class SeguroRForm(forms.Form):
# 	class Meta:
# 		model = SeguroR
# 		fields = ['marca', 'modelo', 'ano', 'descripcion', 'pasajeros', 'estadoCirculacion']

