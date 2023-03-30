from django.shortcuts import render
from django.http import HttpResponse
from App1.models import Curso, Profesor, estudiante, tareas
from App1.forms import CursoFormulario, Vendedorformulario, Clienteformulario, Productoformulario
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView    
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from App1.forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

@login_required
def inicio(request):
    return render(request, 'index.html')


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request , data = request.POST)
        if form.is_valid():
            usuario = form .cleaned_data.get('username')
            contras = form.cleaned_data.get ('password')

            user = authenticate(username = usuario, password= contras)
            if user is not None:
                login(request, user)
                return render(request, "index.html", {"mensaje":f"BIenvenido {usuario}"})
            else:
                return render(request, "index.html", {"mensaje":"error, datos incorrectos"})
        else:
            return render(request, "index.html", {"mensaje":"error, formulario erroneo."})
    form= AuthenticationForm()
    return render(request, "login.html", {"form":form})

        
def register(request):
    if request.method == 'POST':
        #form= UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)
        if  form.is_valid():

            username = form.cleaned_data['username']
            form.save()
            return render(request, 'index.html', {'mensaje': 'Usuario Creado:'})
    else:
        #form = UserCreationForm()
        form = UserRegisterForm()
    return render (request, 'registro.html', {'form': form})



       #-----VIEWS CORTITAS-----

#def inicio (request):
 #     return render(request, 'index.html')

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

            #EDITAR 

def editarcurso (request, curso_nombre):
    curso = Curso.objects.get(nombre = curso_nombre)
    if request.method == 'POST':
        miformulario = CursoFormulario(request.POST)
        print(miformulario)

        if miformulario.is_valid:
            informacion = miformulario.cleaned_data

            curso.nombre = informacion['nombre']
            curso.camada = informacion['camada']

            curso.save()
            return render(request, "index.html")
    else:
        miformulario = CursoFormulario(initial={'nombre': curso.nombre,
                                                'camada': curso.camada})
        
        return render (request, "editarcurso.html", {"miformulario": miformulario, 
                                                     "curso_nombre": curso_nombre})
    



def editarliente (request, cliente_nombre):
    cliente = estudiante.objects.get(nombre = cliente_nombre)
    if request.method == 'POST':
        miformulario = Clienteformulario(request.POST)
        print(miformulario)

        if miformulario.is_valid:
            informacion = miformulario.cleaned_data

            cliente.nombre= informacion['nombre']
            cliente.apellido= informacion['apellido']
            cliente.email= informacion['email']

            cliente.save()
            return render(request, "index.html")
    
    else:
        miformulario = Clienteformulario(initial={'nombre': cliente.nombre,
                                                  'apellido': cliente.apellido,
                                                  'email': cliente.email})
        
        return render (request, "editarcliente.html", {"miformulario": miformulario,
                                                       "cliente_nombre": cliente_nombre})
    

def editarvendedor (request, vendedor_nombre):
    vendedor= Profesor.objects.get(nombre= vendedor_nombre)
    if request.method == 'POST':
        miformulario = Vendedorformulario(request.POST)
        print(miformulario)

        if miformulario.is_valid:
            informacion = miformulario.cleaned_data

            vendedor.nombre= informacion['nombre']
            vendedor.apellido= informacion['apellido']
            vendedor.email= informacion['email']

            vendedor.save()
            return render(request, "index.html")
        
    else:
        miformulario= Vendedorformulario(initial={'nombre': vendedor.nombre,
                                                  'apellido': vendedor.apellido,
                                                  'email': vendedor.email})
        
        return render(request, "editarvendedor.html", {"miformulario": miformulario,
                                                       "vendedor_nombre": vendedor_nombre})


def editarproducto ( request, producto_nombre):
    producto = tareas.objects.get(nombre= producto_nombre)
    if request.method == 'POST':
        miformulario= Productoformulario(request.POST)
        print(miformulario)

        if miformulario.is_valid:
            informacion =miformulario.cleaned_data

            producto.nombre= informacion['nombre']
            producto.Fechadeentrega= informacion['Fechadeentrega']
            producto.entregado= informacion ['entregado']

            producto.save()
            return render(request, "index.html")
        
    else:
        miformulario= Productoformulario(initial={'nombre': producto.nombre,
                                                  'fechadeentrega': producto.Fechadeentrega,
                                                  'entregado': producto.entregado})
        
        return render(request, "editarvendedor.html", {"miformulario": miformulario,
                                                       "producto_nombre": producto_nombre})
    


class cursolist (ListView):
    model= Curso
    template_name= "curso_list.html"

class cursodetalle (DetailView):
    model= Curso
    template_name= "curso_detalle.html"

class cursocreacion  (CreateView):
    model = Curso
    template_name= "curso_form.html"
    success_url= reverse_lazy("App1:list")
    fields= ['nombre', 'camada']

class cursoupdate (UpdateView):
    model= Curso
    success_url= "/App1/curso/list"
    template_name= "curso_form.html"
    fields= ['nombre', 'camada']

class cursodelete (DeleteView):
    model = Curso 
    template_name= "curso_confirm_delete.html"
    success_url= "/App1/curso/list"

