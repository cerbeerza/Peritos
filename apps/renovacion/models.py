from django.db import models
from django.contrib.auth.models import User

class Renovacion(models.Model):

    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateField(auto_now_add=True)
    periodo = models.CharField(max_length=4)

    def __str__(self):
        return self.id_user






