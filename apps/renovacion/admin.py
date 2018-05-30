from django.contrib import admin
from apps.renovacion.models import Renovacion
from import_export.admin import ImportExportModelAdmin
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.core.files.storage import FileSystemStorage
from weasyprint import HTML
from apps.administration.models import Profile
from django.contrib.auth.models import User


def imprimir_ficha(self, request, queryset):


    lista = list(queryset)
    for objRenov in lista:

        profile = Profile.objects.get(user_id=objRenov.id_user_id)
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
        fecha_proceso = objRenov.fecha_creacion


        dict_ctx = {
                     'nombres': nombres, 'apellidos': apellidos, 'nacionalidad': nacionalidad,
                     'estado_civil': estado_civil, 'rut': rut, 'domicilio': domicilio, 'comuna': comuna,
                     'region': region, 'telefono': telefono, 'celular': celular, 'email': email,
                     'profesion': profesion, 'empresa': empresa, 'diremp': diremp, 'telemp': telemp,
                     'fecha_proceso': fecha_proceso
                   }
        html_string = render_to_string('templates/renovacion/ficha.html', {'dic': dict_ctx})

        html = HTML(string=html_string, base_url=request.build_absolute_uri())
        #html.write_pdf(target='D:/files/pdf.pdf')
        html.write_pdf(target='/Users/ignaciobeltransilva/filesTmp/pdf.pdf')

        #fs = FileSystemStorage('D:/files')
        fs = FileSystemStorage('/Users/ignaciobeltransilva/filesTmp')
        with fs.open('pdf.pdf') as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'
            return response


class RenovacionAdmin(ImportExportModelAdmin):
    list_display = ('id_user', 'get_nombre', 'fecha_creacion', 'periodo')
    list_filter = ['periodo']
    readonly_fields = ['archivo_ci', 'archivo_ant', 'archivo_tit']
    actions = [imprimir_ficha]

    def get_nombre(self, instance):
        return instance.id_user.profile.nombres + " " + instance.id_user.profile.apellido_p + " " + instance.id_user.profile.apellido_m
    get_nombre.short_description = "Nombres"





admin.site.register(Renovacion, RenovacionAdmin)