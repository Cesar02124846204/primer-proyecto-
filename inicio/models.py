from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=20)
    edad= models.IntegerField()
    nacionalidad = models.CharField(max_length=20, blank=True, null=True)
    
    def __str__(self):
        return f"Cliente: {self.nombre} - Edad : {self.edad} - Nacionalidad: {self.nacionalidad}"