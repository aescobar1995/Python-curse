"""Entrega1_AgustinEscobar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import form_Profesores, form_Estudiantes, form_Empleado, mostrar_Profesores, mostrar_Estudiantes, mostrar_Empleado,buscar_estudiante,index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name= "Inicio"),
    path('profesores/', form_Profesores, name= "Profesores"),
    path('mostrarprofesores/', mostrar_Profesores, name= "VerProfesores"),
    path('estudiantes/', form_Estudiantes, name= "Estudiantes"),
    path('mostrarestudiantes/', mostrar_Estudiantes, name= "VerEstudiantes"),
    path('empleado/', form_Empleado, name= "Empleado"),
    path('mostrarempleado/', mostrar_Empleado,name= "VerEmpleado"),
    path('buscarestudiante/', buscar_estudiante, name= "BuscarEstudiantes"),
]
