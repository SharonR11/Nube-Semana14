from django.db import models

class Persona(models.Model):
    idPersona = models.AutoField(primary_key=True, auto_created=True)
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)
    email=models.EmailField()
    fecha_nac= models.DateField()
    foto= models.ImageField(upload_to='fotos')
    celular=models.IntegerField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"