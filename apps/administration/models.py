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
        ('M', 'MASCULINO'),
        ('F', 'FEMENINO'),
    )
    genero = models.CharField(max_length=1, choices=generos, null=True)
    nacionalidad = models.CharField(max_length=20, null=True)
    direccion = models.CharField(max_length=80, null=True)

    region = models.CharField(max_length=50, null=True)
    provincia = models.CharField(max_length=50, null=True)
    comuna = models.CharField(max_length=50, null=True)
    estados_civil = (
        ('SOLTERO', 'SOLTERO(A)'),
        ('CASADO', 'CASADO(A)'),
        ('VIUDO', 'VIUDO(A)'),
    )
    estado_civil = models.CharField(max_length=20, choices=estados_civil, null=True)
    telefono_casa = models.IntegerField(null=True)
    telefono_cel = models.IntegerField(null=True)
    profesiones = (
        ('ingGeoMen', 'Ingeniero en Geomensura'),
        ('ingEjecGeo', 'Ingeniero de Ejecución en Geomensura'),
        ('ingEjecMin', 'Ingeniero de Ejecución en Minas'),
    )
    profesion = models.CharField(max_length=40, null=True)
    universidad = models.CharField(max_length=50, null=True)
    archivo_titulo = models.CharField(max_length=300, blank=True, null=True)
    archivo_ci = models.CharField(max_length=300, blank=True, null=True)
    archivo_ant = models.CharField(max_length=300, blank=True, null=True)
    year_titulo = models.IntegerField(null=True)
    empresa = models.CharField(max_length=50, null=True)
    telefono_empresa = models.IntegerField(null=True)
    direccion_empresa = models.CharField(max_length=80, null=True)



    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()






