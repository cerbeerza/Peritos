from django.db import models


class Usuario(models.Model):
    
    rut = models.CharField(max_length=8, primary_key=True)
    nombres = models.CharField(max_length=50)
    apellido_p = models.CharField(max_length=50)
    apellido_m = models.CharField(max_length=50)
    fecha_nac = models.DateField()
    email = models.EmailField()
    password = models.CharField(max_length=20)

    generos = (
        ('M','MASCULINO'),
        ('F', 'FEMENINO'),
    )
    genero = models.CharField(max_length=1, choices=generos)
    nacionalidad = models.CharField(max_length=20)
    direccion = models.CharField(max_length=80)
    region = models.CharField(max_length=30)
    comuna = models.CharField(max_length=50)
    estados_civil = (
        ('SOLTERO','SOLTERO(A)'),
        ('CASADO','CASADO(A)'),
        ('VIUDO', 'VIUDO(A)'),
    )
    estado_civil = models.CharField(max_length=20, choices=estados_civil)
    telefono_casa = models.IntegerField()
    telefono_cel = models.IntegerField()
    profesiones = (
        ('ingGeoMen', 'Ingeniero en Geomensura'),
        ('ingEjecGeo', 'Ingeniero de Ejecución en Geomensura'),
        ('ingEjecMin', 'Ingeniero de Ejecución en Minas'),
    ) 
    profesion = models.CharField(max_length=40)
    universidad = models.CharField(max_length=50)
    archivo_titulo = models.CharField(max_length=300, blank=True)
    archivo_ci = models.CharField(max_length=300, blank=True)
    archivo_ant = models.CharField(max_length=300, blank=True)
    year_titulo = models.IntegerField()
    empresa = models.CharField(max_length=50)
    telefono_empresa = models.IntegerField()
    direccion_empresa = models.CharField(max_length=80)

    


