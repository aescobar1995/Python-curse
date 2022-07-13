from curses.ascii import HT
from xml.dom import NoModificationAllowedErr
from django.shortcuts import render
from django.http import HttpResponse
from datetime import date, datetime
from mi_app.models import Curso
from mi_app.forms import CursoBusquedaFormulario, CursoFormulario

# Create your views here.

def saludo(request):
    return HttpResponse("Hola mundo")

def mostrar_hora(request):
    fecha_hora_ahora = datetime.now()
    return HttpResponse(f"La hora es: {fecha_hora_ahora}")

def saludar_a(request, nombre):
    return HttpResponse(f"Hola como estas {nombre}")

def mostrar_index(request):
    return render(request, "mi_app/index.html",{"mi_titulo":"Hola este es mi primer website!!!"})


def saludo_personalizado(request):
    context = {}

    if request.GET:
        context["nombre"] = request.GET["nombre"]
    return render(request, "mi_app/index.html", context)

def listar_cursos(request):
    context = {}
    context["cursos"] = Curso.objects.all()
    return render(request, "mi_app/lista_cursos.html", context)

def cursoFormulario(request):
    if request.method == 'POST':
        miFormulario = CursoFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:              # Valida el ingreso del tipo de datos, previamente definidos en el formulario
            informacion = miFormulario.cleaned_data
            curso = Curso(nombre=informacion['curso'],camada=informacion['camada'])
            curso.save()
            return render(request, "mi_app/inicio.html") # Vuelvo a donde se quiera dps de guardar el curso
    else:
        miFormulario= CursoFormulario()  # Si no es POST, formulario vacio para el contexto
    return render(request, "mi_app/inicio.html", {"miFormulario":miFormulario})

def formulario_busqueda(request):
    busqueda_formulario = CursoBusquedaFormulario()
    if request.GET:
        cursos = Curso.objects.filter(nombre=busqueda_formulario["criterio"]).all()
        return render(request, "mi_app/curso_busqueda.html", {"cursos": cursos})
    busqueda_formulario = CursoBusquedaFormulario()
    return render(request,"mi_app/curso_busqueda.html",{"busqueda_formulario":busqueda_formulario})