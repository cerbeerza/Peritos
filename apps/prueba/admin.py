from django.contrib import admin
from apps.prueba.models import Prueba

class PruebaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'rut', 'nota', 'situacion', 'periodo')
    list_filter = ['periodo']

admin.site.register(Prueba, PruebaAdmin)
