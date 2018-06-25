from django.contrib import admin
from apps.postulacion.models import Postulacion
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.models import User
from apps.administration.models import Profile
from django.template.loader import render_to_string
from weasyprint import HTML
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from itertools import cycle


def imprimir_ficha(self, request, queryset):

    lista = list(queryset)
    for objPost in lista:

        profile = Profile.objects.get(user_id=objPost.id_user_id)
        user = User.objects.get(id=profile.user_id)
        nombres = profile.nombres
        apellidos = profile.apellido_p + " " + profile.apellido_m
        nacionalidad = profile.nacionalidad
        estado_civil = profile.estado_civil
        rut = profile.rut
        domicilio = profile.direccion
        comuna = profile.comuna
        region = profile.region
        telefono = profile.telefono_casa
        celular = profile.telefono_cel
        email = user.email
        profesion = profile.profesion
        empresa = profile.empresa
        diremp = profile.direccion_empresa
        telemp = profile.telefono_empresa
        fecha_proceso = objPost.fecha_creacion
        region_examen = objPost.region_examen

        dv = digito_verificador(rut)
        if dv == 10:
            dv = 'K'


        dict_ctx = {
            'nombres': nombres, 'apellidos': apellidos, 'nacionalidad': nacionalidad,
            'estado_civil': estado_civil, 'rut': rut, 'domicilio': domicilio, 'comuna': comuna,
            'region': region, 'telefono': telefono, 'celular': celular, 'email': email,
            'profesion': profesion, 'empresa': empresa, 'diremp': diremp, 'telemp': telemp,
            'fecha_proceso': fecha_proceso, 'region_examen': region_examen, 'dv': dv
        }


        html_string = render_to_string('templates/postulacion/ficha.html', {'dic': dict_ctx})
        html = HTML(string=html_string, base_url=request.build_absolute_uri())
        html.write_pdf(target='D:/files/pdf.pdf')
        #html.write_pdf(target='/home/files/pdf.pdf')
        #html.write_pdf(target='/Users/ignaciobeltransilva/filesTmp/pdf.pdf')

        fs = FileSystemStorage('D:/files')
        # fs = FileSystemStorage('/home/files')
        #fs = FileSystemStorage('/Users/ignaciobeltransilva/filesTmp')
        with fs.open('pdf.pdf') as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'
            return response

class PostulacionAdmin(ImportExportModelAdmin):
    list_display = ('id_user', 'get_nombre', 'fecha_creacion', 'periodo', 'region_examen')
    list_filter = ['periodo']
    actions = [imprimir_ficha]


    def get_nombre(self, instance):
        return instance.id_user.profile.nombres + " " + instance.id_user.profile.apellido_p + " " + instance.id_user.profile.apellido_m
    get_nombre.short_description = "Nombres"


admin.site.register(Postulacion, PostulacionAdmin)


def digito_verificador(rut):
    reversed_digits = map(int, reversed(str(rut)))
    factors = cycle(range(2, 8))
    s = sum(d * f for d, f in zip(reversed_digits, factors))
    return (-s) % 11
