from django.urls import path
from . import views
#se importa url views a busqueda de directorio raiz blog
urlpatterns = [
    
    
    path('',views.blog,name='blog'),
    #se agrega visualizacion de categoria por lectura de bbdd
    path('categoria/<categoria_id>',views.categoria,name='categoria')
    

]