from django.urls import path
from .views import ListViewTicket, DetailViewTicket, CreateViewTicket, CreateViewSugerencia, ListViewSugerencia,ListViewMisTickets
from . import views

urlpatterns = [
    path('', ListViewTicket.as_view(), name='bandeja-inicio'),
    path('ticket/<int:pk>/', DetailViewTicket.as_view(), name='ticket-detail'),
    path('ticket/nuevo/', CreateViewTicket.as_view(), name='ticket-create'),
    path('mis-tickets/', ListViewMisTickets.as_view(), name="mis-tickets"),
    path('sugerencias/', CreateViewSugerencia.as_view(), name="sugerencias"),
    path('bandeja-sugerencias/', ListViewSugerencia.as_view(), name="bandeja-sugerencias"),
]