from django.db import models


class Curso (models.Model):

    nombre =models.CharField(max_length=30)
    camada =models.IntegerField()

class estudiante (models.Model):
    nombre =models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

class profesor (models.Model):
    nombre =models.CharField(max_length=30)
    apellido =models.CharField(max_length=30)
    email =models.EmailField()

class tareas (models.Model):
    nombre= models.CharField(max_length=30)
    fechadeentrega =models.DateField()
    entregado = models.BooleanField()

