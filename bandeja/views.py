from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from .models import Ticket


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
    fields = ['titulo', 'descripcion']

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)
