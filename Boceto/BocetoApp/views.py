from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.http import HttpResponse
from .models import Post


# Create your views here.

def home(request):  
   return render(request, "boceto/home.html")

def base(request):  
   return render(request, "boceto/base.html")


def enviar_correo(request):
    enviado_correctamente = False# Variable que va a determinar si se envió el correo correctamente , nos servira para el if del template
    if request.method == 'POST':
        email = request.POST.get('email', '')  # Obtenemos el correo electrónico ingresado por el usuario en home.html
         # Ahora enviamos el correo electrónico
        subject = 'Gracias por ponerte en contacto con nosotros'
        message = f'Hola,\n\nGracias por ponerte en contacto con nosotros. Pronto te responderemos.\n\nAtentamente,\nEl equipo de Cooperativa Oro Verde \nEste canal fue creado para compartir informacion escencial \npara tu funcionamiento en nuestra plataforma.Los mensajes son automaticos,\npor lo tanto no podremos responder tus comentarios por esta via'
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
   #le enviamos la variable posts que almacena todos los posts subidos para asi poder recorrerlos en un for 
   return render(request, "boceto/noticias.html", {"posts": posts})


"""en esta funcion le enviamos como parametro la id de la noticia
creamos una variable noticia que obtendra de post la id de los post hechos
nos retorno un archivo html que nos mostrara la notica completa """
def ver_noticia(request, noticia_id):
    """
    The function "ver_noticia" retrieves a specific news article based on its ID and renders it in a
    template.
    
    :param request: The request object represents the HTTP request that the user made to access the
    view. It contains information such as the user's browser details, the requested URL, and any data
    sent with the request
    :param noticia_id: The `noticia_id` parameter is the unique identifier of the news article that the
    user wants to view. It is used to retrieve the specific news article from the database using the
    `get_object_or_404` function
    :return: a rendered HTML template called 'ver_noticia.html' with the context data of the 'noticia'
    object.
    """

    noticia = get_object_or_404(Post, id=noticia_id)

    return render(request, 'boceto/ver_noticia.html', {'noticia': noticia})