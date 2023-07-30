from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
from .models import Post


# Create your views here.

def home(request):  
   return render(request, "boceto/home.html")

def base(request):  
   return render(request, "boceto/base.html")


def enviar_correo(request):
    enviado_correctamente = False  # Variable que va a determinar si se envió el correo correctamente , nos servira para el if del template

    if request.method == 'POST':
        email = request.POST.get('email', '')  # Obtenemos el correo electrónico ingresado por el usuario en home.html
         # Ahora enviamos el correo electrónico
        subject = 'Gracias por ponerte en contacto con nosotros'
        message = f'Hola,\n\nGracias por ponerte en contacto con nosotros. Pronto te responderemos.\n\nAtentamente,\nEl equipo de Cooperativa Oro Verde'
        from_email = email  # le mandamos la variable email para que envie el mensaje al correo ingresado por el usuario como remitente
        recipient_list = [email]
        try:
            send_mail(subject, message, from_email, recipient_list)
            enviado_correctamente = True  # Actualizamos el valor de la variable a True si se envió correctamente
        except Exception as e:
            pass  # No es necesario hacer nada aquí, la variable seguirá siendo False

    # Enviamos el valor de "enviado_correctamente" como parte del contexto para usarlo en el if 
    return render(request, 'boceto/home.html', {'enviado_correctamente': enviado_correctamente})

"""creamos una variable llamada posts y le enviamos todo lo que contenga la clase Post creada en models.py
y le mandamos en el return los posts"""
def noticias(request):  
    
   posts=Post.objects.all()
   return render(request, "boceto/noticias.html", {"posts": posts})
