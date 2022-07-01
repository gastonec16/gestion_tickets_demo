from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Ticket(models.Model):
    titulo = models.CharField('Título', max_length=100)
    descripcion = models.TextField('Descripción', max_length=5000)
    fecha = models.DateTimeField(default=timezone.now)
    autor = models.ForeignKey(User, on_delete=models.RESTRICT)
    area = models.CharField('Área', max_length=100, blank=True, default='')
    pc = models.CharField('PC', max_length=100, blank=True, default='')
    componente = models.CharField(max_length=100, blank=True, default='')

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('ticket-detail', kwargs={'pk': self.pk})

class Sugerencia(models.Model):
    mensaje = models.TextField()
    fecha = models.DateTimeField(default=timezone.now)
    autor = models.ForeignKey(User, on_delete=models.RESTRICT)

    def __str__(self):
        return f'{self.autor.first_name} {self.autor.last_name}'

    def get_absolute_url(self):
        return reverse('bandeja-inicio')
