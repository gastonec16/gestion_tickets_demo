from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Perfil

class FormRegistroUsuario(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    legajo = forms.IntegerField()
    telefono = forms.IntegerField(label='Teléfono', required=False)
    is_staff = forms.BooleanField(label='Es del equipo técnico', required=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'legajo', 'telefono', 'password1', 'password2', 'is_staff']

class FormActualizarUsuario(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class FormActualizarPerfil(forms.ModelForm):
    telefono = forms.IntegerField(label='Teléfono', required=False)

    class Meta:
        model = Perfil
        fields = ['imagen', 'legajo', 'telefono']