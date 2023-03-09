from django.urls import path
from App1 import views

urlpatterns = [
    path('', views.inicio, name= 'inicio'),
    path('curso/', views.cursos, name= 'curso'),
    path('profesores/', views.profesores, name= 'profesores'),
    path('estudiantes/', views.estudiantes, name= 'estudiantes'),
    path('tareas/', views.tareas, name= 'tareas'),
    path('cursoformulario', views.cursoformulario, name='Cursoformulario')
]
