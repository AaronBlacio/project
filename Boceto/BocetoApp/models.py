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


class Cotizacion(models.Model):
    """
    Modelo para almacenar solicitudes de cotización de clientes.
    
    Campos:
        - nombre: Nombre completo del cliente
        - empresa: Nombre de la empresa (opcional)
        - email: Correo electrónico del cliente
        - telefono: Teléfono de contacto
        - pais: País del cliente
        - cantidad: Cantidad aproximada de cajas por semana
        - mensaje: Mensaje o requerimientos especiales
        - created: Fecha de la solicitud
        - atendida: Si la solicitud fue procesada
    """
    PAISES_CHOICES = [
        ('DE', '🇩🇪 Alemania'),
        ('FR', '🇫🇷 Francia'),
        ('IT', '🇮🇹 Italia'),
        ('ES', '🇪🇸 España'),
        ('NL', '🇳🇱 Países Bajos'),
        ('BE', '🇧🇪 Bélgica'),
        ('UK', '🇬🇧 Reino Unido'),
        ('US', '🇺🇸 Estados Unidos'),
        ('JP', '🇯🇵 Japón'),
        ('OTHER', '🌍 Otro'),
    ]
    
    nombre = models.CharField(max_length=200, verbose_name='Nombre completo')
    empresa = models.CharField(max_length=200, blank=True, verbose_name='Empresa')
    email = models.EmailField(verbose_name='Correo electrónico')
    telefono = models.CharField(max_length=50, blank=True, verbose_name='Teléfono')
    pais = models.CharField(max_length=10, choices=PAISES_CHOICES, verbose_name='País')
    cantidad = models.CharField(max_length=100, verbose_name='Cantidad aproximada (cajas/semana)')
    mensaje = models.TextField(blank=True, verbose_name='Mensaje adicional')
    
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de solicitud')
    atendida = models.BooleanField(default=False, verbose_name='¿Atendida?')
    
    class Meta:
        verbose_name = 'cotización'
        verbose_name_plural = 'cotizaciones'
        ordering = ['-created']
    
    def __str__(self):
        return f"Cotización de {self.nombre} - {self.empresa or 'Sin empresa'}"


class Testimonial(models.Model):
    """
    Modelo para testimoniales de clientes europeos.
    
    Campos:
        - nombre: Nombre del cliente
        - empresa: Empresa del cliente
        - pais: País del cliente
        - cargo: Cargo en la empresa
        - testimonio: Texto del testimonio
        - imagen: Foto del cliente (opcional)
        - rating: Calificación de 1-5 estrellas
        - activo: Si se muestra en el sitio
    """
    nombre = models.CharField(max_length=200, verbose_name='Nombre')
    empresa = models.CharField(max_length=200, verbose_name='Empresa')
    pais = models.CharField(max_length=100, verbose_name='País')
    cargo = models.CharField(max_length=200, blank=True, verbose_name='Cargo')
    testimonio = models.TextField(verbose_name='Testimonio')
    imagen = models.ImageField(
        upload_to='testimonials/', 
        null=True, 
        blank=True,
        verbose_name='Foto'
    )
    rating = models.PositiveSmallIntegerField(
        default=5,
        verbose_name='Calificación (1-5)'
    )
    activo = models.BooleanField(default=True, verbose_name='¿Mostrar en sitio?')
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'testimonial'
        verbose_name_plural = 'testimoniales'
        ordering = ['-created']
    
    def __str__(self):
        return f"{self.nombre} - {self.empresa} ({self.pais})"
