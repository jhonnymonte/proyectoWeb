from django.shortcuts import render
from servicios.models import Servicio

# Create your views here.

def servicios(request):
    #importo todos los objetos dentro de la class servicios
    servicios=Servicio.objects.all()
    return render(request,"servicios/servicios.html",{'servicios':servicios})
