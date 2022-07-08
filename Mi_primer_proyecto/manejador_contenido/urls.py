from django.contrib import admin
from django.urls import path
from manejador_contenido.views import mostrar_home, mostrar_profile

urlpatterns = [
    path('home/', mostrar_home),
    path('profile/', mostrar_profile),
]
