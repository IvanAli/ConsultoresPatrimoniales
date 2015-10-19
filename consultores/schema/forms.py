from django import forms
from django.forms import ModelForm
from .models import Usuario

class LoginForm(forms.Form):
    user = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30)
