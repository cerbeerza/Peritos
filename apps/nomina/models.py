from django.db import models

class Nomina(models.Model):

    rut_nomina = models.CharField(max_length=11)
    nombre_nomina = models.CharField(max_length=50)
    periodo = models.CharField(max_length=4)

    def __str__(self):
        return self.nombre_nomina


