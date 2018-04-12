from django.db import models
from django.contrib.auth.models import User

class Apelacion(models.Model):

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateField(auto_now_add=True)
    periodo = models.CharField(max_length=4)
    desc_apelacion = models.CharField(max_length=300)




