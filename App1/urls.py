from django.urls import path
from App1 import views


urlpatterns = [
    path('', views.inicio, name= 'inicio'),
    path('cursos/', views.cursos, name= 'cursos'),
    path('vendedor/', views.vendedor, name= 'vendedor'),
    path('clientes/', views.clientes, name= 'clientes'),
    path('productos/', views.productos, name= 'productos'),
    #path('cursoformulario', views.Cursoformulario, name='Cursoformulario'),
    #path('vendedorformulario', views.vendedorformulario, name='Vendedorformulario'),
    #path('clienteformulario', views.clienteformulario, name='Clienteformulario'),
    #path('productoformulario/', views.productoformulario, name='Productoformulario'),
    path('busquedacamada/', views.busquedacamada, name='BusquedaCamada'),
    path('buscar/', views.buscar),
    path('leercursos/', views.leercursos, name= 'Leercursos'),
    path('leerclientes/', views.leerclientes, name= 'Leerclientes'),
    path('leervendedor/', views.leervendedor, name='Leervendedor'),
    path('leerproductos/', views.leerproductos, name='Leerproducto'),
    path('eliminarcurso/<curso_nombre>/', views.eliminarcurso, name='Eliminarcurso'),
    path('eliminarcliente/<cliente_nombre>/', views.eliminarcliente, name='Eliminarcliente'),
    path('eliminarvendedor/<vendedor_nombre>/', views.eliminarvendedor, name='Eliminarvendedor'),
    path('eliminarproductos/<producto_nombre>/', views.eliminarproducto, name='Eliminarproducto'),
    ]

#prueba