from django.contrib import admin
from apps.prueba.models import Prueba
from import_export.admin import ImportExportModelAdmin

class PruebaAdmin(ImportExportModelAdmin):
    list_display = ('nombre', 'rut', 'nota', 'situacion', 'periodo')
    list_filter = ['periodo']


admin.site.register(Prueba, PruebaAdmin)
