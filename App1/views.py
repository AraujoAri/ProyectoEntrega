from django.shortcuts import render
from django.http import HttpResponse


def inicio (request):
    return HttpResponse('estamos en inicio')

def cursos (request):
    return HttpResponse('estamos en cursos')

def profesores (request):
    return HttpResponse('estamos en profesores')

def estudiantes (request):
    return HttpResponse ('estamos en estudiantes')

def tareas (request):
    return HttpResponse('estamos en tareas')
