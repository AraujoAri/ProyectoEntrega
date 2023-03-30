from django.urls import path
from App1 import views
from django.contrib.auth.views import LogoutView


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
    path('editarcurso/<curso_nombre>/', views.editarcurso, name='Editarcurso'),  # type: ignore
    path('editarcliente/<cliente_nombre>/', views.editarliente, name='Editarcliente'),  # type: ignore
    path('editarvendedor/<vendedor_nombre>/', views.editarvendedor, name='Editarvendedor'), # type: ignore
    path('editarproducto/<producto_nombre>/', views.editarproducto, name= 'Editarproducto'),  # type: ignore
    path('curso/list', views.cursolist.as_view(), name='list'),
    path('nuevo', views.cursocreacion.as_view(), name='new'),
    path('borrar/<int:pk>', views.cursodelete.as_view(), name='delete'),
    path('editar/<int:pk>', views.cursoupdate.as_view(), name='Editar'), # type: ignore
    path('<int:pk>', views.cursodetalle.as_view(), name='Detalle'), # type: ignore
    path('login', views.login_request, name='login'),  # type: ignore
    path('register', views.register, name='Register'),
    path('logout', LogoutView.as_view(template_name='logout.html'), name='Logout'),  # type: ignore
    ]

#prueba