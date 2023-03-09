from django import forms



class CursoFormulario(forms.Form):

    nombre= forms.CharField()
    camada= forms.IntegerField( )


class Vendedorformulario (forms.Form):
    nombre =forms.CharField(max_length=30)            
    apellido =forms.CharField(max_length=30)
    email =forms.EmailField()


class Clienteformulario (forms.Form):
    nombre =forms.CharField(max_length=30)         
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()


class Productoformulario (forms.Form):
    nombre= forms.CharField(max_length=30)
    cantidad =forms.IntegerField()                 
    numdeserie = forms.IntegerField()