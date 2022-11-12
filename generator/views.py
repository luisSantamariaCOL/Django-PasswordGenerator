from django.http import HttpResponse
from django.shortcuts import render
import random

def home(request):
    return render(request, 'generator/home.html')

# Parámetro request: recibimos información de la petición que está llegando
def about(request): 
    # render lee un archivo y lo devuelve al usuario
    return render(request, 'generator/about.html')

def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')
    generated_password = ''

    # Recibiremos el valor que aparezca en la url en la variable length
    length_in_url = 'length'
    password_length = int(request.GET.get(length_in_url))

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
  
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()_+'))

    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    for _ in range(password_length):
        generated_password += random.choice(characters)

    return render(request, 'generator/password.html', {'password': generated_password})