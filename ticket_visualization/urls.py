from django.urls import path
from ticket_visualization import views

urlpatterns = [
    path('', views.home),
    path('display_tickets', views.display_tickets, name='display_tickets'),
    path('get_tickets', views.get_tickets, name='get_tickets')
]
