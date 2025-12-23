from django.urls import path
from BocetoApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # Páginas principales
    path("", views.home, name="index"),
    path("base/", views.base, name="base"),
    path("Nosotros/", views.nosotros, name="nosotros"),
    path("Colaboradores/", views.colaboradores, name="colaboradores"),
    path("Labor_social/", views.labor, name="labor"),
    path("Bana_Pan/", views.banapan, name="banapan"),
    path("Cooporoverdesa/", views.cooporoverdesa, name="cooporoverdesa"),
    
    # Contacto y Cotización
    path("enviado/", views.enviar_correo, name="enviar_correo"),
    path("cotizacion/", views.cotizacion, name="cotizacion"),
    path("cotizacion/enviar/", views.enviar_cotizacion, name="enviar_cotizacion"),
    
    # Noticias
    path("noticias/", views.noticias, name="noticias"),
    path("noticia/<int:noticia_id>/", views.ver_noticia, name="ver_noticia"),
]

# Servir archivos multimedia en desarrollo
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)