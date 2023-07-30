from django.urls import path
from BocetoApp import views

urlpatterns = [
   
    path('',views.home, name="index"),
    path('base/',views.base, name="base"),
    path('/', views.enviar_correo, name='enviar_correo'),
    path('noticias/', views.noticias, name='noticias'),


       
]