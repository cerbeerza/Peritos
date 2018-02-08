from django.db import models

class Region(models.Model):

    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=80)
    cod_region = models.CharField(max_length=2)


class Provincia(models.Model):

    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=80)
    id_region = models.ForeignKey(Region, on_delete=models.CASCADE)
    cod_provincia = models.CharField(max_length=3)

class Comuna(models.Model):

    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=80)
    id_provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)
    cod_comuna = models.CharField(max_length=4)












