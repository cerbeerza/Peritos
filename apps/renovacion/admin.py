from django.contrib import admin
from apps.renovacion.models import Renovacion



class RenovacionAdmin(admin.ModelAdmin):
    list_display = ('id_user', 'get_nombre', 'fecha_creacion', 'periodo')
    list_filter = ['periodo']
    readonly_fields = ['archivo_ci', 'archivo_ant', 'archivo_tit']

    def get_nombre(self, instance):
        return instance.id_user.profile.nombres
    get_nombre.short_description = "Nombres"





admin.site.register(Renovacion, RenovacionAdmin)