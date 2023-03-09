from django.shortcuts import render
from django.http import HttpResponse
from App1.models import Curso


def inicio (request):
    return render(request, 'index.html')

def cursos (request):
    return render(request, 'cursos.html')

def doctores (request):
    return render(request, 'doctores.html')

def pacientes (request):
    return render(request, 'pacientes.html')

def turnos (request):
    return render(request, 'turnos.html')

def cursoformulario(request):
    if request.method == 'POST':

        curso= Curso(request.POST['nombre'], request.POST['camada'])
        curso.save()

        return render(request, 'inicio.html')
    
    return render(request, 'cursoformulario.html')
