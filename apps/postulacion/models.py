from django.db import models
from django.contrib.auth.models import User

class Postulacion(models.Model):

    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateField(auto_now_add=True)
    periodo = models.CharField(max_length=4)
    region_examen = models.CharField(max_length=40)

    def __str__(self):
        return self.id_user







