from django.db import models
from django.contrib.auth.models import User
from apps.administration.models import Profile

class Postulacion(models.Model):

    class Meta:
        verbose_name = 'Postulación'
        verbose_name_plural = 'Postulaciones'

    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateField(auto_now_add=True)
    periodo = models.CharField(max_length=4)
    region_examen = models.CharField(max_length=40)

    def __str__(self):
        userProfile = Profile.objects.get(user_id=self.id_user)
        return userProfile.nombres + " " + userProfile.apellido_p + " " + userProfile.apellido_m







