from django.db import models

class PeriodoProceso(models.Model):

    periodo = models.CharField(max_length=9)
    fechaDesde = models.DateField()
    fechaHasta = models.DateField()

    def __str__(self):
        return self.periodo


