from django.db import models

from apps.usuario.models import Usuario 


class MensuraGeneral(models.Model):
    
    periodo = models.CharField(max_length=4)
    num_mensura = models.IntegerField()
    promedio = models.FloatField()
    empresa = models.CharField(max_length=40)
    situacion = models.CharField(max_length=20)
    usuario = models.ForeignKey(Usuario)


    
