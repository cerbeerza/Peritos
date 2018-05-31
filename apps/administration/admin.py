from django.contrib import admin
from apps.administration.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    search_fields = ['nombres']
    list_display = ('nombres', 'apellido_p', 'apellido_m', 'rut')


admin.site.register(Profile, ProfileAdmin)