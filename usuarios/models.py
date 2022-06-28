from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=150, default='Nombre')
    apellido = models.CharField(max_length=150, default='Apellido')
    imagen = models.ImageField(default='perfil-default.jpg', upload_to='fotos-perfil')
    legajo = models.IntegerField(blank=True, null=True)
    telefono = models.IntegerField(blank=True, null=True)

    def __str__(self) -> str:
        return f'Perfil de {self.usuario.username}'
