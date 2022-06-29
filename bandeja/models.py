from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Ticket(models.Model):
    titulo = models.CharField('Título', max_length=100)
    descripcion = models.TextField('Descripción', max_length=5000)
    fecha = models.DateTimeField(default=timezone.now)
    autor = models.ForeignKey(User, on_delete=models.RESTRICT)
    area = models.CharField('Área', max_length=100, blank=True, null=True)
    pc = models.CharField('PC', max_length=100, blank=True, null=True)
    componente = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('ticket-detail', kwargs={'pk': self.pk})
