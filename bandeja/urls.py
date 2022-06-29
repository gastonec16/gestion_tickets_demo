from django.urls import path
from .views import ListViewTicket, DetailViewTicket, CreateViewTicket, CreateViewSugerencia
from . import views

urlpatterns = [
    path('', ListViewTicket.as_view(), name='bandeja-inicio'),
    path('ticket/<int:pk>/', DetailViewTicket.as_view(), name='ticket-detail'),
    path('ticket/nuevo/', CreateViewTicket.as_view(), name='ticket-create'),
    path('mis-tickets/', views.mis_tickets, name="mis-tickets"),
    path('sugerencias/', CreateViewSugerencia.as_view(), name="sugerencias"),
    path('bandeja-sugerencias/', views.bandeja_sugerencias, name="bandeja-sugerencias"),
]