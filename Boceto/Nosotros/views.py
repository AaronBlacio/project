from django.shortcuts import render


# Create your views here.
def Nosotros(request):
    return render(request, "Nosotros/nosotros.html")
