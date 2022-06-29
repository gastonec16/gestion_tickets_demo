from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import FormRegistroUsuario, FormActualizarUsuario, FormActualizarPerfil

def registrarse(request):
    if request.method == 'POST':
        form = FormRegistroUsuario(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Su cuenta se ha registrado. Ahora puede iniciar sesión')
            return redirect('iniciar-sesion')
    else:
        form = FormRegistroUsuario()
    return render(request, 'usuarios/registrarse.html', {'form': form})

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