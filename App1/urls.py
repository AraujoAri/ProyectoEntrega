from django.urls import path
from App1 import views

urlpatterns = [
    path('', views.inicio, name= 'inicio'),
    path('curso/', views.cursos, name= 'curso'),
    path('doctores/', views.doctores, name= 'doctores'),
    path('pacientes/', views.pacientes, name= 'pacientes'),
    path('turnos/', views.turnos, name= 'turnos'),
    path('cursoformulario', views.cursoformulario, name='Cursoformulario')
]
