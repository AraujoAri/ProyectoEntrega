from django.shortcuts import render
from django.http import HttpResponse
from App1.models import Curso
from App1.forms import CursoFormulario


       #-----VIEWS CORTITAS-----

def inicio (request):
    return render(request, 'index.html')

def cursos (request):
    return render(request, 'cursos.html')

def vendedor (request):
    return render(request, 'vendedor.html')

def clientes (request):
    return render(request, 'clientes.html')

def productos (request):
    return render(request, 'productos.html')



        #---FORMULARIOS----

def Cursoformulario(request): 
    if request.method == 'POST':
        miformulario = CursoFormulario(request.POST)
        print(miformulario)

        if miformulario.is_valid:
            informacion = miformulario.cleaned_data

            curso = Curso(nombre=informacion['nombre'], camada=informacion['camada'])
            curso.save()

            return render(request, 'index.html')
    else:
        miformulario =CursoFormulario()
    return render(request, 'cursoformulario.html', {'miformulario': miformulario})
