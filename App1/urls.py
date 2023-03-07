from django.urls import path
from App1 import views

urlpatterns = [
    path('', views.inicio),
    path('profe/', views.profesores),
    path('curso/', views.cursos),
    path('estudiantes/', views.estudiantes),
    path('tareas/', views.tareas),
]
