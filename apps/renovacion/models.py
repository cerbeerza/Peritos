from django.db import models
from django.contrib.auth.models import User
from datetime import date
from apps.periodo.models import PeriodoProceso


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    fecha_actual = date.today()
    # fecha_actual = '2019-07-01'
    objetoPeriodo = PeriodoProceso.objects.get(fechaDesde__lte=fecha_actual,
                                               fechaHasta__gte=fecha_actual)
    periodo = objetoPeriodo.periodo
    year = periodo[0:4]

    return year+'/'+'user_{0}/{1}'.format(instance.id_user, filename.replace(' ', ''))


class Renovacion(models.Model):

    class Meta:
        verbose_name = 'Renovación'
        verbose_name_plural = 'Renovaciones'

    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateField(auto_now_add=True)
    periodo = models.CharField(max_length=4)
    archivo_ci = models.FileField(upload_to=user_directory_path, null=True)
    archivo_ant = models.FileField(upload_to=user_directory_path, null=True)
    archivo_tit = models.FileField(upload_to=user_directory_path, null=True)

    def __str__(self):
        return str(self.id_user)






