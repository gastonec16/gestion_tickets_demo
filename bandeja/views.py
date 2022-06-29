from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from .models import Sugerencia, Ticket


def inicio(request):
    context = {
        'tickets': Ticket.objects.all()
    }
    return render(request, 'bandeja/inicio.html', context)

def mis_tickets(request):
    context = {
        'tickets': Ticket.objects.all()
    }
    return render(request, 'bandeja/mis-tickets.html', context)

class ListViewTicket(ListView):
    model = Ticket
    template_name = "bandeja/inicio.html"
    context_object_name = 'tickets'
    ordering = ['-fecha']

class DetailViewTicket(DetailView):
    model = Ticket

class CreateViewTicket(LoginRequiredMixin, CreateView):
    model = Ticket
    fields = ['titulo', 'descripcion', 'area', 'pc', 'componente']

    def form_valid(self, form):
        form.instance.autor = self.request.user
        messages.success(self.request, f'¡Su ticket ha sido enviado!')
        return super().form_valid(form)

def bandeja_sugerencias(request):
    context = {
        'sugerencias': Sugerencia.objects.all()
    }
    return render(request, 'bandeja/bandeja-sugerencias.html', context)

class CreateViewSugerencia(LoginRequiredMixin, CreateView):
    model = Sugerencia
    fields = ['mensaje']

    def form_valid(self, form):
        form.instance.autor = self.request.user
        messages.success(self.request, f'Se ha enviado su sugerencia. ¡Muchas gracias!')
        return super().form_valid(form)
