from django.shortcuts import render
from . models import Producto

# Create your views here.
def tienda(request):

    Productos=Producto.objects.all()

    return render(request,"tienda/tienda.html",{"productos":Productos})
