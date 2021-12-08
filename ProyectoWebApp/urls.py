from django.urls import path

from ProyectoWebApp import views
#se importa config para visualizacion de imagenes
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('',views.home,name='home'),
    

]
#se agrega url para visualizar imagenes
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)