from django.contrib import admin
from apps.administration.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    search_fields = ['nombres']


admin.site.register(Profile, ProfileAdmin)