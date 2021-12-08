from django.db import models


# Create your models here.
#creamos mapeo orm para la segunda app web

class Servicio(models.Model):
    titulo=models.CharField(max_length=50)
    contenido=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to='servicios')
    created=models.DateTimeField(auto_now_add=True) #crea fecha automaticamente
    updated=models.DateTimeField(auto_now_add=True) #modifica fecha automaticamente
    #creo subclase verbose
    class Meta:
        
        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'
    #retorno titulo
    def __str__(self):
        return self.titulo

    #se realizan las migraciones en terminal
    #manage.py makemigrations
    #manage.py migrate

