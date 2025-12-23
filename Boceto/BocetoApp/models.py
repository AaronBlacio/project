from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Modelo para publicaciones de noticias/blog de la Cooperativa.
    
    Campos:
        - titulo: Título de la publicación (máx. 200 caracteres)
        - contenido: Contenido completo de la publicación (sin límite)
        - imagen: Imagen opcional para la publicación
        - autor: Usuario que creó la publicación
        - created: Fecha y hora de creación (automático)
        - updated: Fecha y hora de última actualización (automático)
    """
    id = models.BigAutoField(primary_key=True)
    titulo = models.CharField(max_length=200, verbose_name='Título')
    contenido = models.TextField(verbose_name='Contenido')  # Cambiado a TextField para contenido extenso
    imagen = models.ImageField(
        upload_to='posts/', 
        null=True, 
        blank=True, 
        verbose_name='Imagen'
    )
    autor = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        verbose_name='Autor'
    )
    
    # ✅ CORREGIDO: auto_now=True actualiza la fecha en cada guardado
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Última actualización')

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        ordering = ['-created']  # Ordenar por más recientes primero

    def __str__(self):
        return self.titulo


