from django.shortcuts import render
from django.http import HttpResponse


def inicio (request):
    return render(request, 'inicio.html')

def cursos (request):
    return render(request, 'cursos.html')

def profesores (request):
    return render(request, 'profesores.html')

def estudiantes (request):
    return render(request, 'estudiantes.html')

def tareas (request):
    return render(request, 'tareas.html')
