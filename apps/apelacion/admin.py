from django.contrib import admin
from apps.apelacion.models import Apelacion


def responde_apelacion(self, request, queryset):

    lista = list(queryset)



class ApelacionAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'periodo','fecha_creacion')
    #actions = []



admin.site.register(Apelacion, ApelacionAdmin)
