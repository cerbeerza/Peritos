from django.contrib import admin
from apps.postulacion.models import Postulacion
from import_export.admin import ImportExportModelAdmin

class PostulacionAdmin(ImportExportModelAdmin):
    list_display = ('id_user', 'get_nombre', 'fecha_creacion', 'periodo', 'region_examen')
    list_filter = ['periodo']

    def get_nombre(self, instance):
        return instance.id_user.profile.nombres + " " + instance.id_user.profile.apellido_p + " " + instance.id_user.profile.apellido_m
    get_nombre.short_description = "Nombres"




admin.site.register(Postulacion, PostulacionAdmin)
