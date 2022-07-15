from django.shortcuts import render
from app.forms import  formProfesores, formEstudiantes,formEmpleado,form_busqueda_estudiantes
from app.models import Profesor, Estudiante, Empleado
from django.db.models import Q
# Create your views here.

def index(request):
    return render (request, "app/index.html", {})

def form_Profesores(request):

    if request.method == 'POST':
        formProf = formProfesores(request.POST)

        if formProf.is_valid():
            informacion = formProf.cleaned_data
            profesor = Profesor (nombre = informacion["nombre"], apellido = informacion["apellido"], dni = informacion["dni"], asignatura = informacion["asignatura"])
            profesor.save()
            chequeo = print ("Se ha registrado con exito el formulario. Muchas Gracias")
            return render (request, "app/profesores.html")
    else:
        formProf = formProfesores()
        return render (request, "app/profesores.html",{"formProf":formProf})


def form_Estudiantes(request):

    if request.method == 'POST':
        formEstu = formEstudiantes(request.POST)

        if formEstu.is_valid():
            data = formEstu.cleaned_data
            estudiante = Estudiante (nombre = data["nombre"], apellido = data["apellido"], dni = data["dni"], curso = data["curso"])
            estudiante.save()
            chequeo = print ("Se ha registrado con exito el formulario. Muchas Gracias")
            return render (request, "app/estudiantes.html")
    else:
        formEstu = formEstudiantes()
        return render (request, "app/estudiantes.html",{"formEstu":formEstu})



def form_Empleado(request):

    if request.method == 'POST':
        formEmpl = formEmpleado(request.POST)

        if  formEmpl.is_valid():
            data =  formEmpl.cleaned_data
            empleado = Empleado (nombre = data["nombre"], apellido = data["apellido"], dni = data["dni"], sector = data["sector"])
            empleado.save()
            chequeo = print ("Se ha registrado con exito el formulario. Muchas Gracias")
            return render (request, "app/empleado.html")
    else:
        formEmpl = formEmpleado()
        return render (request, "app/empleado.html",{"formEmpl":formEmpl})

def mostrar_Profesores(request):

    profesores = Profesor.objects.all()
    return render (request,  "app/mostrarProfesores.html", {"profesores": profesores})


def mostrar_Estudiantes(request):

    estudiantes = Estudiante.objects.all()
    return render (request,  "app/mostrarEstudiantes.html", {"estudiantes": estudiantes})


def mostrar_Empleado(request):

    empleado = Empleado.objects.all()
    return render (request,  "app/mostrarEmpleado.html", {"empleado": empleado})

def buscar_estudiante(request):

    formularioEs = form_busqueda_estudiantes()

    if request.GET:
        
        resultado = Estudiante.objects.filter(nombre=request.GET["criterio"]).all()
    
    else:
        resultado = []

        
    return render (request, "app/busquedaEstudiantes.html", {"formularioEs" : formularioEs, "resultado" : resultado})