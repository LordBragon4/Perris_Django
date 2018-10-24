from django import forms
from .models import Mascota

class RegistrarPersona(forms.Form):
    rutPersona=forms.CharField(widget=forms.TextInput(),label="Rut")
    passwordPersona=forms.CharField(widget=forms.PasswordInput(),label="Contraseña")
    nombrePersona=forms.CharField(widget=forms.TextInput(),label="Nombre")
    apellidoPersona=forms.CharField(widget=forms.TextInput(),label="Apellido")
    #        Arreglar FECHA NACIMIENTO
    fechaNacimiento=forms.DateField(widget=forms.DateInput(),label="Fecha de Nacimiento")
    #-------------------------------------
    direccionPersona=forms.CharField(widget=forms.TextInput(),label="Direccion")
    numeroFono=forms.CharField(widget=forms.TextInput(),label="Telefono")
    mailPersona=forms.EmailField(label="Email: ")

class RegistrarMascota(forms. Form):

    class meta:
        model = Mascota
        fields = ['imagenMascota']