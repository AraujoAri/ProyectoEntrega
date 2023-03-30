from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



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
    Fechadeentrega =forms.DateField()                 
    entregado = forms.BooleanField()


class UserRegisterForm (UserCreationForm):
    email = forms.CharField()
    password1 = forms.CharField(label='contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_text = {k:"" for k in fields}
        