from django.contrib import admin
from apps.zona.models import Region, Provincia, Comuna

admin.site.register(Region)
admin.site.register(Provincia)
admin.site.register(Comuna)

