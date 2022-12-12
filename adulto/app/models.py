from django.db import models

# Create your models here.


class Instructor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    

    def __str__(self):
        return self.nombre
    
class Taller(models.Model):
    nombre=models.CharField(max_length=50)
    descripcion=models.TextField(max_length=250)
    Instructor=models.ForeignKey(Instructor,on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="taller", null=True)
    cupos = models.IntegerField()
    
    
    def __str__(self):
        return self.nombre