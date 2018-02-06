from django.db import models


class MensuraGeneral(models.Model):

    periodo = models.CharField(max_length=4)
    num_mensura = models.IntegerField()
    promedio = models.FloatField()
    empresa = models.CharField(max_length=40)
    situacion = models.CharField(max_length=20)
    usuario_id = models.CharField(max_length=10)

    def __str__(self):
        return self.usuario_id







