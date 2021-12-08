from django.shortcuts import redirect, render
from .forms import FormularioContacto
from django.core.mail import EmailMessage




# Create your views here.
def contacto(request):
    formulario_contacto=FormularioContacto#instanciamos la vista dentro de la funcion contacto!
    if request.method=="POST":
        formulario_contacto=FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")
            #construccion de envio de mail desde django
            email=EmailMessage("Mensaje desde Django",
            "el usuario {} con direccion  {} escribio lo siguiente:\n {}".format(nombre,email,contenido),"",["email in settings"],reply_to=[email])
            
            try:
                email.send()
                return redirect("/?valido")
            except:
                return redirect("/?novalido")
            
    return render(request,"contacto/contacto.html",{'miFormulario':formulario_contacto})