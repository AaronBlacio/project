from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.http import HttpResponse
from .models import Post


# Create your views here.
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


def enviar_correo(request):
    enviado_correctamente = False  # Variable que va a determinar si se envió el correo correctamente , nos servira para el if del template
    if request.method == "POST":
        email = request.POST.get(
            "email", ""
        )  # Obtenemos el correo electrónico ingresado por el usuario en home.html
        # Ahora enviamos el correo electrónico
        subject = "Gracias por ponerte en contacto con nosotros"
        message = f"Hola,\n\nGracias por ponerte en contacto con nosotros. Pronto te responderemos.\n\nAtentamente,\nEl equipo de Cooperativa Oro Verde \nEste canal fue creado para compartir informacion escencial \npara tu funcionamiento en nuestra plataforma.Los mensajes son automaticos,\npor lo tanto no podremos responder tus comentarios por esta via"
        from_email = email  # le mandamos la variable email para que envie el mensaje al correo ingresado por el usuario como remitente
        recipient_list = [email]
        try:
            send_mail(subject, message, from_email, recipient_list)
            enviado_correctamente = True  # Actualizamos el valor de la variable a True si se envió correctamente
        except Exception as e:
            pass  # No es necesario hacer nada aquí, la variable seguirá siendo False

    # Enviamos el valor de "enviado_correctamente" como parte del contexto para usarlo en el if
    return render(
        request, "boceto/home.html", {"enviado_correctamente": enviado_correctamente}
    )


"""creamos una variable llamada posts y le enviamos todo lo que contenga la clase Post creada en models.py
y le mandamos en el return los posts"""



def noticias(request):
    posts = Post.objects.all()
    # le enviamos la variable posts que almacena todos los posts subidos para asi poder recorrerlos en un for
    return render(request, "boceto/noticias.html", {"posts": posts})



"""en esta funcion le enviamos como parametro la id de la noticia
creamos una variable noticia que obtendra de post la id de los post hechos
nos retorno un archivo html que nos mostrara la notica completa """

def ver_noticia(request, noticia_id):
    """
     La función "ver_noticia" recupera un artículo de noticias específico basado en su ID y lo presenta en un
     plantilla.

     :param request: El objeto request representa la solicitud HTTP que el usuario realizó para acceder al
     vista. Contiene información como los detalles del navegador del usuario, la URL solicitada y cualquier dato
     enviado con la solicitud
     :param noticia_id: El parámetro `noticia_id` es el identificador único de la noticia que
     usuario quiere ver. Se utiliza para recuperar el artículo de noticias específico de la base de datos utilizando el
     Función `get_object_or_404`
     :return: una plantilla HTML renderizada llamada 'ver_noticia.html' con los datos de contexto de la 'noticia'
     objeto.
     """
    noticia = get_object_or_404(Post, id=noticia_id)

    return render(request, "boceto/ver_noticia.html", {"noticia": noticia})
