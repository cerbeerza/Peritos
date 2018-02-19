from django.db import models

class Prueba(models.Model):

    rut = models.CharField(max_length=10)
    nombre = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    parte_a = models.CharField(max_length=5)
    parte_b = models.CharField(max_length=5)
    parte_final = models.CharField(max_length=5)
    nota = models.CharField(max_length=5)
    situacion = models.CharField(max_length=20)
    periodo = models.CharField(max_length=4)
    rutx = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre
