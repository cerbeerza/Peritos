from django.db import models
from django.contrib.auth.models import User

class Renovacion(models.Model):

    class Meta:
        verbose_name = 'Renovación'
        verbose_name_plural = 'Renovaciones'

    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateField(auto_now_add=True)
    periodo = models.CharField(max_length=4)
    archivo_ci = models.FileField(upload_to='ci/', null=True)
    archivo_ant = models.FileField(upload_to='ant/', null=True)
    archivo_tit =models.FileField(upload_to='tit/', null=True)



    def __str__(self):
        return str(self.id_user)






