from django.shortcuts import render
# Importamos http response 
from django.http import HttpResponse


# Create your views here.
def hola_mundo(request):
    # Devolvemos un hola mundo atraves de un encabezado h1
    return HttpResponse("<h1>Hola mundo desde mi aplicación web</h1><br><p>Esta es una prueba de parrafo</p>")

# Crear vista principal 
def inicio(request):
    return render(request, 'base.html')