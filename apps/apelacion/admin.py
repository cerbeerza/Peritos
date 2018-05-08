from django.contrib import admin
from apps.apelacion.models import Apelacion

class ApelacionAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'periodo','fecha_creacion')

admin.site.register(Apelacion, ApelacionAdmin)