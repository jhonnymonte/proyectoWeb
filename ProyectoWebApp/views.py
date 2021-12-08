from django.shortcuts import render


# Create your views here.
#renderizo por template los html

def home(request):
    return render(request,"ProyectoWebApp/home.html")






    

