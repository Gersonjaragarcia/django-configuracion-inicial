from django.shortcuts import render
from django.http import HttpResponse

# Creamos nuestra primera vista
def home(request):
    return HttpResponse("<h1>¡Hola! Este es mi inicio en Django </h1>")
