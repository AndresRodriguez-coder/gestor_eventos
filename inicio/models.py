from django.db import models

# Create your models here.
class Eventos (models.Model):
    nombre=models.CharField(max_length=50)
    descripcion= models.TextField()
    nomb_org=models.CharField(100)
    cont_org=models.IntegerField()
    fecha=models.DateTimeField()
    lugar=models.CharField(max_length=50)
    
