from django.contrib import admin
from .models import Servicio

# Register your models here.

#creo clase para visualizacion de fechas
class ServicioAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
#registro el sitio
admin.site.register(Servicio,ServicioAdmin)