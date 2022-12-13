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
    Instructor=models.ForeignKey(Instructor,on_delete=models.PROTECT)
    imagen = models.ImageField(upload_to="taller", null=True)
    cupos = models.IntegerField()
    curso = models.BooleanField(default=False)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    horario = models.TextField()
    
    
    def __str__(self):
        return self.nombre
    
class postulaciones(models.Model):
        nombre = models.CharField(max_length=50)
        apellido = models.CharField(max_length=50)
        email = models.EmailField(max_length=50)
        direccion = models.TextField(max_length=250)
        villa = models.CharField(max_length=50)
        telefono = models.IntegerField()
        genero = models.CharField(max_length=50)
        Taller = models.ForeignKey(Taller,on_delete=models.CASCADE)
        fecha = models.DateField()
        
        def __str__(self):
            return self.nombre