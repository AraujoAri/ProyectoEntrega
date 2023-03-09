from django.urls import path
from App1 import views



urlpatterns = [
    path('', views.inicio, name= 'inicio'),
    path('curso/', views.cursos, name= 'curso'),
    path('vendedor/', views.vendedor, name= 'vendedor'),
    path('clientes/', views.clientes, name= 'clientes'),
    path('productos/', views.productos, name= 'productos'),
    path('cursoformulario', views.Cursoformulario, name='Cursoformulario'),
    path('vendedorformulario', views.vendedorformulario, name='Vendedorformulario'),
    path('clienteformulario', views.clienteformulario, name='Clienteformulario'),
    path('productoformulario/', views.productoformulario, name='Productoformulario')
]
