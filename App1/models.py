from django.db import models


     #----NUESTROS MODELOS A SEGUIR-----

class Curso (models.Model):
    id =models.AutoField(primary_key=True)            #ESTO CRRESPONDE A ---CURSOS---
    nombre =models.CharField(max_length=30)
    camada =models.IntegerField()

class estudiante (models.Model):
    nombre =models.CharField(max_length=30)           #ESTO CORRESPONDE A LO QUE AHORA ES ---CLIENTES---
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

class Profesor (models.Model):
    nombre =models.CharField(max_length=30)            #ESTO CORRESPONDE A LO QUE AHORA ES ---VENDEDOR---
    apellido =models.CharField(max_length=30)
    email =models.EmailField()

class tareas (models.Model):
    nombre= models.CharField(max_length=30)
    Fechadeentrega =models.DateField()                 #ESTO CORRESPONDE A LO QUE AHORA ES ---PRODUCTOS---
    entregado = models.BooleanField()

