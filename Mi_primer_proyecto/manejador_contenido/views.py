from django.shortcuts import render

# Create your views here.

def mostrar_home(request):
    return render(request, "manejador_contenido/home.html", {})

def mostrar_profile(request):
    return render(request, "manejador_contenido/profile.html", {})