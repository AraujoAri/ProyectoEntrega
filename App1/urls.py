from django.urls import path
from App1 import views

urlpatterns = [
    path('', views.inicio),
    path('curso/', views.cursos),
    path('profesores/', views.profesores),
    path('estudiantes/', views.estudiantes),
    path('tareas/', views.tareas),
]
