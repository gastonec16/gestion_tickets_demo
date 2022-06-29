from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Perfil

class FormRegistroUsuario(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(label='Nombre', required=True)
    last_name = forms.CharField(label='Apellido', required=True)
    legajo = forms.IntegerField()
    telefono = forms.IntegerField(label='Teléfono', required=False)
    is_staff = forms.BooleanField(label='Es del equipo técnico', required=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'legajo', 'telefono', 'password1', 'password2', 'is_staff']

class FormActualizarUsuario(forms.ModelForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(label='Nombre', required=True)
    last_name = forms.CharField(label='Apellido', required=True)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class FormActualizarPerfil(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['imagen', 'legajo', 'telefono']