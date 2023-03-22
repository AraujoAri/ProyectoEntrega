from django.db import models


     #----NUESTROS MODELOS A SEGUIR-----

class Curso (models.Model):           
    nombre =models.CharField(max_length=30)          #ESTO CRRESPONDE A ---CURSOS---
    camada =models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Camada: {self.camada}"

class estudiante (models.Model):
    nombre =models.CharField(max_length=30)           #ESTO CORRESPONDE A LO QUE AHORA ES ---CLIENTES---
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Email: {self.email}"

class Profesor (models.Model):
    nombre =models.CharField(max_length=30)            #ESTO CORRESPONDE A LO QUE AHORA ES ---VENDEDOR---
    apellido =models.CharField(max_length=30)
    email =models.EmailField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Email: {self.email}"

class tareas (models.Model):
    nombre= models.CharField(max_length=30)
    Fechadeentrega =models.DateField()                 #ESTO CORRESPONDE A LO QUE AHORA ES ---PRODUCTOS---
    entregado = models.BooleanField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Fecha: {self.Fechadeentrega} - Entregado: {self.entregado}"
        #la funcion de lo que esta arriba es mostras los datos en el "admin" y facilitar su lectura

