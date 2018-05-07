from django.contrib import admin
from apps.nomina.models import Nomina


class NominaAdmin(admin.ModelAdmin):
    list_display = ('nombre_nomina', 'rut_nomina', 'periodo')
    list_filter = ['periodo']


admin.site.register(Nomina, NominaAdmin)

