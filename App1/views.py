from django.shortcuts import render
from django.http import HttpResponse
from App1.models import Curso, Profesor, estudiante, tareas
from App1.forms import CursoFormulario, Vendedorformulario, Clienteformulario, Productoformulario


       #-----VIEWS CORTITAS-----

def inicio (request):
    return render(request, 'index.html')

#def cursos (request):
 #   return render(request, 'cursos.html')

#def vendedor (request):
#    return render(request, 'vendedor.html')

#def clientes (request):
#   return render(request, 'clientes.html')

#def productos (request):
#    return render(request, 'productos.html')



        #---FORMULARIOS----

def cursos(request): 
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
    return render(request, 'cursos.html', {'miformulario': miformulario})





def vendedor (request):
    if request.method == 'POST':
        miformulario = Vendedorformulario(request.POST)
        print(miformulario)
        if miformulario.is_valid:
            informacion= miformulario.cleaned_data
            vendedor = Profesor(nombre=informacion['nombre'],
                                apellido=informacion['apellido'],
                                email=informacion['email'])
            vendedor.save()
            return render(request, 'index.html')
    else:
        miformulario = Vendedorformulario()
    return render(request, 'vendedor.html', {'miformulario': miformulario})





def clientes (request):
    if request.method == 'POST':
        miformulario = Clienteformulario(request.POST)
        print(miformulario)
        if miformulario.is_valid:
            informacion=miformulario.cleaned_data
            cliente= estudiante(nombre=informacion['nombre'],
                                apellido=informacion['apellido'],
                                email=informacion['email'])
            cliente.save()
            return render(request, 'index.html')
    else:
        miformulario= Clienteformulario()
    return render(request, 'clientes.html', {'miformulario': miformulario})



def productos (request):
    if request.method == 'POST':
        miformulario = Productoformulario(request.POST)
        print(miformulario)
        if miformulario.is_valid:
            informacion=miformulario.cleaned_data
            producto= tareas(nombre=informacion['nombre'],
                             Fechadeentrega=informacion['Fechadeentrega'],
                             entregado=informacion['entregado'])
            producto.save()
            return render(request, 'index.html')
    else:
        miformulario=Productoformulario()
    return render(request, 'productos.html', {'miformulario': miformulario})




def busquedacamada(request):
    return render(request, 'busquedacamada.html')


def buscar (request):
    if request.GET['camada']:
        camada =request.GET['camada']
        curso = Curso.objects.filter(camada__icontains=camada)

        return render(request, 'index.html', {"curso": cursos, "camada": camada})
    else:
        respuesta ="No enviaste datos"

    #return HttpResponse(respuesta)
    return render(request, 'index.html', {"respuesta": respuesta})



def leercursos (request):
    cursos = Curso.objects.all()
    contexto = {"cursos": cursos}
    return render(request, "leercursos.html", contexto)

def leerclientes (request):
    clientes = estudiante.objects.all()
    contexto = {"clientes": clientes}
    return render (request, "leerclientes.html", contexto)

def leervendedor (request):
    vendedor = Profesor.objects.all()
    contexto = {"vendedor": vendedor}
    return render (request, "leervendedor.html", contexto)

def leerproductos (request):
    productos = tareas.objects.all()
    contexto = {"productos": productos}
    return render (request, "leerproductos.html", contexto)


         #ELIMINAR 

def eliminarcurso(request, curso_nombre):
    curso = Curso.objects.get(nombre= curso_nombre)
    curso.delete()

    cursos = Curso.objects.all()
    contexto = {"cursos": cursos}
    return render(request, "leercursos.html", contexto)



def eliminarcliente ( request, cliente_nombre):
    cliente= estudiante.objects.get(nombre = cliente_nombre)
    cliente.delete()

    clientes = estudiante.objects.all()
    contexto = {"clientes": clientes}
    return render(request, "leerclientes.html", contexto)


def eliminarvendedor(request, vendedor_nombre):
    vendedor= Profesor.objects.get(nombre= vendedor_nombre)
    vendedor.delete()

    vendedors= Profesor.objects.all()
    contexto= {"vendedors": vendedors}
    return render(request, "leervendedor.html", contexto)


def eliminarproducto(request, producto_nombre):
    producto = tareas.objects.get(nombre= producto_nombre)
    producto.delete()

    productos = tareas.objects.all()
    contexto = {"productos": productos}
    return render(request, "leerproductos.html", contexto)