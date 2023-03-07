from django.shortcuts import render
from App1.models import Curso
from django.http import HttpResponse

def curso (self):

    curso1 = Curso(nombre='desarrollo web', camada=123)
    curso1.save()

    documentodetexto = f'--->curso: {curso1.nombre} y camada: {curso1.camada}'
    
    return HttpResponse(documentodetexto)

#w