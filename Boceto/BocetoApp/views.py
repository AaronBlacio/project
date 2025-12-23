from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.http import HttpResponse, Http404
from django.views.decorators.http import require_POST
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.conf import settings
import logging

from .models import Post

# Configurar logger para errores de email
logger = logging.getLogger(__name__)


# ============================================
# 🏠 VISTAS PRINCIPALES
# ============================================

def home(request):
    """Vista de la página principal."""
    return render(request, "boceto/home.html")

def base(request):
    """Vista de la plantilla base."""
    return render(request, "boceto/base.html")

def nosotros(request):
    """Vista de la página Nosotros."""
    return render(request, "boceto/nosotros.html")

def colaboradores(request):
    """Vista de la página de Colaboradores."""
    return render(request, "boceto/colaboradores.html")

def labor(request):
    """Vista de la página de Labor Social."""
    return render(request, "boceto/labor.html")

def banapan(request):
    """Vista de la página de Bana Pan."""
    return render(request, "boceto/banapan.html")

def cooporoverdesa(request):
    """Vista de la página de Cooporoverdesa."""
    return render(request, "boceto/cooporoverdesa.html")


# ============================================
# 📧 VISTA DE CONTACTO CON VALIDACIÓN
# ============================================

@require_POST
def enviar_correo(request):
    """
    Procesa el formulario de contacto y envía un correo de confirmación.
    
    Validaciones implementadas:
    - Verifica que el email no esté vacío
    - Valida el formato del email usando Django validators
    - Usa el email configurado como remitente (no el del usuario)
    - Registra errores en el log para debugging
    """
    enviado_correctamente = False
    error_mensaje = None
    email = request.POST.get('email', '').strip()
    
    # ✅ VALIDACIÓN 1: Email no vacío
    if not email:
        error_mensaje = "Por favor, ingresa tu correo electrónico."
        return render(request, 'boceto/home.html', {
            'enviado_correctamente': False,
            'error_mensaje': error_mensaje
        })
    
    # ✅ VALIDACIÓN 2: Formato de email válido
    try:
        validate_email(email)
    except ValidationError:
        error_mensaje = "El correo electrónico ingresado no es válido."
        return render(request, 'boceto/home.html', {
            'enviado_correctamente': False,
            'error_mensaje': error_mensaje
        })
    
    # Configurar el correo
    subject = 'Gracias por ponerte en contacto con nosotros - Cooperativa Oro Verde'
    message = f"""
Hola,

Gracias por ponerte en contacto con nosotros. Hemos recibido tu mensaje
y pronto te responderemos.

Tu correo: {email}

Atentamente,
El equipo de Cooperativa Agrícola Oro Verde
🍌 Produciendo banano orgánico con comercio justo
    """.strip()
    
    # ✅ CORRECCIÓN: Usar el email configurado como remitente
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]

    try:
        send_mail(
            subject=subject,
            message=message,
            from_email=from_email,
            recipient_list=recipient_list,
            fail_silently=False  # Para capturar errores
        )
        enviado_correctamente = True
        logger.info(f"Correo enviado exitosamente a: {email}")
        
    except Exception as e:
        error_mensaje = "Hubo un problema al enviar el correo. Por favor, intenta más tarde."
        logger.error(f"Error al enviar correo a {email}: {str(e)}")
        enviado_correctamente = False

    return render(request, 'boceto/home.html', {
        'enviado_correctamente': enviado_correctamente,
        'error_mensaje': error_mensaje
    })


# ============================================
# 📰 VISTAS DE NOTICIAS
# ============================================

def noticias(request):
    """Vista que muestra todas las noticias/posts."""
    posts = Post.objects.all()
    return render(request, "boceto/noticias.html", {"posts": posts})

def ver_noticia(request, noticia_id):
    """Vista para ver el detalle de una noticia específica."""
    noticia = get_object_or_404(Post, id=noticia_id)
    return render(request, "boceto/ver_noticia.html", {"noticia": noticia})

