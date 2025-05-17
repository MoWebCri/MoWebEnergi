from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('servicios/', views.servicios, name='servicios'),
    path('calderas/', views.calderas, name='calderas'),
    path('contacto/', views.contacto, name='contacto'),
    path('sobre-nosotros/', views.sobre_nosotros, name='sobre_nosotros'),
] 