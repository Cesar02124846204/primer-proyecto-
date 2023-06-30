from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=20)
    edad= models.IntegerField()
    nacionalidad = models.CharField(max_length=20, blank=True, null=True)