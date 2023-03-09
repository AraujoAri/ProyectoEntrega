from django.shortcuts import render
from django.http import HttpResponse
from App1.models import Curso


def inicio (request):
    return render(request, 'index.html')

def cursos (request):
    return render(request, 'cursos.html')

def profesores (request):
    return render(request, 'profesores.html')

def estudiantes (request):
    return render(request, 'estudiantes.html')

def tareas (request):
    return render(request, 'tareas.html')

def cursoformulario(request):
    if request.method == 'POST':

        curso= Curso(request.POST['nombre'], request.POST['camada'])
        curso.save()

        return render(request, 'inicio.html')
    
    return render(request, 'cursoformulario.html')
