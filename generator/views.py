from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'generator/home.html')

# Parámetro request: recibimos información de la petición que está llegando
def about(request): 
    # render lee un archivo y lo devuelve al usuario
    return render(request, 'generator/about.html')