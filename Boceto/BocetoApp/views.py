from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.http import HttpResponse, Http404
from django.views.decorators.http import require_POST
from django.core.exceptions import ValidationError
from .models import Post
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Vistas para renderizar HTML
def home(request):
    return render(request, "boceto/home.html")

def base(request):
    return render(request, "boceto/base.html")

def nosotros(request):
    return render(request, "boceto/nosotros.html")

def colaboradores(request):
    return render(request, "boceto/colaboradores.html")

def labor(request):
    return render(request, "boceto/labor.html")

def banapan(request):
    return render(request, "boceto/banapan.html")

def cooporoverdesa(request):
    return render(request, "boceto/cooporoverdesa.html")

# Vista para enviar correo
@require_POST
def enviar_correo(request):
    enviado_correctamente = False
    email = request.POST.get('email', '')
    subject = 'Gracias por ponerte en contacto con nosotros'
    message = f'Hola,\n\nGracias por ponerte en contacto con nosotros. Pronto te responderemos.\n\nAtentamente,\nEl equipo de Cooperativa Oro Verde'
    from_email = email
    recipient_list = [email]

    try:
        send_mail(subject, message, from_email, recipient_list)
        enviado_correctamente = True
    except ValidationError as e:
        print(f"Error al enviar correo: {e}")
        enviado_correctamente = False

    return render(request, 'boceto/home.html', {'enviado_correctamente': enviado_correctamente})

# Vista para mostrar noticias
def noticias(request):
    posts = Post.objects.all()
    return render(request, "boceto/noticias.html", {"posts": posts})

# Vista para ver una noticia específica
def ver_noticia(request, noticia_id):
    noticia = get_object_or_404(Post, id=noticia_id)
    return render(request, "boceto/ver_noticia.html", {"noticia": noticia})

