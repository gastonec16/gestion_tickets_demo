from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(default='perfil-default.jpg', upload_to='fotos-perfil')
    legajo = models.IntegerField(blank=True, null=True)
    telefono = models.IntegerField('Teléfono', blank=True, null=True)

    def __str__(self) -> str:
        return f'Perfil de {self.usuario.username}'
