from django.db import models

# Create your models here.

class Meseros(models.Model):
    nombre = models.CharField(max_length=25, default='')
    edad = models.IntegerField()
    procedencia = models.CharField(max_length=25, default='')
