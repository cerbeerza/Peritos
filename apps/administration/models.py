from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from apps.zona.models import Region, Provincia, Comuna






class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombres = models.CharField(max_length=50, null=True)
    apellido_p = models.CharField(max_length=50, null=True)
    apellido_m = models.CharField(max_length=50, null=True)
    fecha_nac = models.DateField(null=True)
    rut = models.CharField(max_length=10, null=True)
    generos = (
        ('S', 'Seleccione'),
        ('M', 'MASCULINO'),
        ('F', 'FEMENINO'),
    )
    genero = models.CharField(max_length=1, choices=generos, null=True, default='S')
    nacionalidad = models.CharField(max_length=20, null=True)
    direccion = models.CharField(max_length=80, null=True)

    region = models.CharField(max_length=50, null=True)
    provincia = models.CharField(max_length=50, null=True)
    comuna = models.CharField(max_length=50, null=True)
    estados_civil = (
        ('-1', 'Seleccione'),
        ('SOLTERO', 'SOLTERO(A)'),
        ('CASADO', 'CASADO(A)'),
        ('VIUDO', 'VIUDO(A)'),
        ('DIVORCIADO', 'DIVORCIADO(A)'),
    )
    estado_civil = models.CharField(max_length=20, choices=estados_civil, null=True, default='Seleccione')
    telefono_casa = models.CharField(null=True, max_length=20)
    telefono_cel = models.CharField(null=True, max_length=20)
    profesiones = (
        ('-1', 'Seleccione'),
        ('ingGeoMen', 'Ingeniero en Geomensura'),
        ('ingEjecGeo', 'Ingeniero de Ejecución en Geomensura'),
        ('ingEjecMin', 'Ingeniero de Ejecución en Minas'),
    )
    profesion = models.CharField(max_length=40, null=True, choices=profesiones, default='Seleccione')
    universidad = models.CharField(max_length=50, null=True)
    archivo_titulo = models.FileField(null=True, blank=True)
    archivo_ci = models.FileField(upload_to='Archivo/', null=True, blank=True)
    archivo_ant = models.FileField(null=True, blank=True)
    year_titulo = models.IntegerField(null=True)
    empresa = models.CharField(max_length=50, null=True)
    telefono_empresa = models.CharField(null=True, max_length=20)
    direccion_empresa = models.CharField(max_length=80, null=True)






    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()






