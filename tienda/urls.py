from django.urls import path

from . import views
#se importa config para visualizacion de imagenes

urlpatterns = [
    
    
    path('',views.tienda,name='tienda'),
    

]
