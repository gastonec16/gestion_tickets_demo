from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Perfil

class FormRegistroUsuario(UserCreationForm):
    email = forms.EmailField()
    is_staff = forms.BooleanField(label='Es del equipo técnico', required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'is_staff']

class FormRegistroPerfil(forms.ModelForm):
    nombre = forms.CharField()
    apellido = forms.CharField()
    legajo = forms.IntegerField()
    telefono = forms.IntegerField(label='Teléfono', required=False)

    class Meta:
        model = Perfil
        fields = ['nombre', 'apellido', 'legajo', 'telefono']

class FormActualizarUsuario(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class FormActualizarPerfil(forms.ModelForm):
    telefono = forms.IntegerField(label='Teléfono', required=False)

    class Meta:
        model = Perfil
        fields = ['nombre', 'apellido', 'imagen', 'legajo', 'telefono']