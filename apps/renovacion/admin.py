from django.contrib import admin
from apps.renovacion.models import Renovacion
from import_export.admin import ImportExportModelAdmin
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.core.files.storage import FileSystemStorage
from weasyprint import HTML








def imprimir_ficha(self, request, queryset):


    lista = list(queryset)
    for objRenov in lista:
        html_string = render_to_string('templates/renovacion/ficha.html', {'algo': 'algo'})

        html = HTML(string=html_string)
        html.write_pdf(target='D:/files/pdf.pdf')

        fs = FileSystemStorage('D:/files')
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