from django.contrib import admin
from django.urls import path
from mi_app.views import saludo, saludar_a, mostrar_hora, listar_cursos, mostrar_index, saludo_personalizado

urlpatterns = [
    path('saludar/', saludo),
    path('saludar/persona/<nombre>', saludar_a),
    path('mostrarhora/', mostrar_hora),
    path('saludo_personalizado/', saludo_personalizado),
    path('lista_cursos/', listar_cursos),
    path('mi_pagina/', mostrar_index),
]
