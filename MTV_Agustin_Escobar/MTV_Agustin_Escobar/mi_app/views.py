from django.shortcuts import render
from mi_app.models import Familia

# Create your views here.


def mostrar_familiares(request):
    context = {}
    context["familia"] = Familia.objects.all()
    return render(request, "mi_app/mostrar_familia.html", context)