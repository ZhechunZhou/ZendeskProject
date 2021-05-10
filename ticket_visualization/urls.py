from django.urls import path
from ticket_visualization import views

urlpatterns =[
    path('', views.home),
    path('display_tickets', views.display_tickets),
]
