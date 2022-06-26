from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(default='perfil-default.jpg', upload_to='fotos-perfil')
    legajo = models.IntegerField(blank=True, null=True)
    telefono = models.IntegerField(blank=True, null=True)

    def __str__(self) -> str:
        return f'Perfil de {self.usuario.username}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.imagen.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.imagen.path)