from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import FormRegistroUsuario, FormRegistroPerfil, FormActualizarUsuario, FormActualizarPerfil
from .models import User

def registrarse(request):
    if request.method == 'POST':
        form_usuario = FormRegistroUsuario(request.POST)
        form_perfil = FormRegistroPerfil(request.POST)
        if form_usuario.is_valid() and form_perfil.is_valid():
            form_usuario.save()
            usuario = form_usuario.cleaned_data.get('username')
            # form_perfil.save()
            messages.success(request, 'Su cuenta se ha registrado. Ahora puede iniciar sesión')
            return redirect('iniciar-sesion')
    else:
        form_usuario = FormRegistroUsuario()
        form_perfil = FormRegistroPerfil()

    context = {
        'form_usuario': form_usuario,
        'form_perfil': form_perfil
    }

    return render(request, 'usuarios/registrarse.html', context)

@login_required
def perfil(request):
    
    if request.method == 'POST':
        form_usuario = FormActualizarUsuario(request.POST, instance=request.user)
        form_perfil = FormActualizarPerfil(request.POST, request.FILES, instance=request.user.perfil)
        
        if form_usuario.is_valid() and form_perfil.is_valid():
            form_usuario.save()
            form_perfil.save()
            messages.success(request, f'Su información se ha actualizado')
            return redirect('perfil')

    else:
        form_usuario = FormActualizarUsuario(instance=request.user)
        form_perfil = FormActualizarPerfil(instance=request.user.perfil)

    context = {
        'form_usuario': form_usuario,
        'form_perfil': form_perfil
    }

    return render(request, 'usuarios/perfil.html', context)