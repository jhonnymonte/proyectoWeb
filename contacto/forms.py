from django import forms
from django.forms.widgets import Textarea




class FormularioContacto(forms.Form):

    
    nombre=forms.CharField(label='Nombre', required=True)
    email=forms.EmailField(label='Email', required=True)
    contenido=forms.CharField(label='Contenido',widget=forms.Textarea, required=False)


    