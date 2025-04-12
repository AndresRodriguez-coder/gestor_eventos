from django.db import models

# Create your models here.
class Evento (models.Model):
    nombre=models.CharField(max_length=50, verbose_name="Nombre del Evento" )
    descripcion= models.TextField(verbose_name="Descripcion del Evento")
    nomb_org=models.CharField(verbose_name="Nombre del Organizador")
    cont_org=models.BigIntegerField(verbose_name="Contacto Del Organizador")
    fecha=models.DateField(verbose_name="Fecha del Evento")
    lugar=models.CharField(max_length=50, verbose_name="Ubicacion")
    imagen=models.ImageField(upload_to='eventos/', blank=True, null=True)
    
