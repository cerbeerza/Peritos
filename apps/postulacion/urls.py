from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from apps.postulacion.views import crea_postulacion

urlpatterns = [
    url(r'^postular$', crea_postulacion, name='postulacion_crear'),
]

