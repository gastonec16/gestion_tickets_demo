"""gestion_tickets_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from usuarios import views as usuarios_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registrarse/', usuarios_views.registrarse, name="registrarse"),
    path('perfil/', usuarios_views.perfil, name="perfil"),
    path('iniciar-sesion/', auth_views.LoginView.as_view(template_name='usuarios/iniciar-sesion.html'), name="iniciar-sesion"),
    path('iniciar-sesion/', auth_views.LoginView.as_view(template_name='usuarios/iniciar-sesion.html'), name="iniciar-sesion"),
    path('cerrar-sesion/', auth_views.LogoutView.as_view(template_name='usuarios/cerrar-sesion.html'), name="cerrar-sesion"),
    path('', include('bandeja.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
