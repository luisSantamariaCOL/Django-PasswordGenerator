from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'generator/home.html')

# Parámetro request: recibimos información de la petición que está llegando
def about(request): 
    # render lee un archivo y lo devuelve al usuario
    return render(request, 'generator/about.html')

def password(request):
    return render(request, 'generator/password.html')