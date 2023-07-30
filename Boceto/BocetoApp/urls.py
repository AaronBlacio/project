from django.urls import path
from BocetoApp import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
   
    path('',views.home, name="index"),
    path('base/',views.base, name="base"),
    path('', views.enviar_correo, name='enviar_correo'),
    path('noticias/', views.noticias, name='noticias'),
      
]
"""urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) es una configuración necesaria para 
que Django pueda servir archivos de medios durante el desarrollo de tu aplicación. 
Permite acceder y mostrar los archivos multimedia cargados por los usuarios a través de sus respectivas URL.en fin nos sirve para 
cargar imagenes en noticias"""
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)