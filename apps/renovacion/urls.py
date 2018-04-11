from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from apps.renovacion.views import renueva

urlpatterns = [
    url(r'^renovar$', renueva, name='postulacion_crear'),
]