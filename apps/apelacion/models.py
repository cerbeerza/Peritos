from django.db import models
from django.contrib.auth.models import User

class Apelacion(models.Model):

    class Meta:
        verbose_name = 'Apelación'
        verbose_name_plural = 'Apelaciones'

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateField(auto_now_add=True)
    periodo = models.CharField(max_length=4)
    desc_apelacion = models.TextField()
    respuesta = models.TextField(null=True, blank=True)














