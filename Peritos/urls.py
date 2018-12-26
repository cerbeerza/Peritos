"""Peritos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from Peritos.views import login_page, registro_page, getProvincia, getComuna, homepage_view, logout_view, editar_datos, reset_password, cambiar_password, notas_generales, notas_generales_det, notas_generales_det2, descargaTodo, responde_reclamacion
from apps.apelacion.views import apelacion
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', login_page, name="login"),
    url(r'^logout/', logout_view, name="logout"),
    url(r'^registro/', registro_page, name="registro"),
    url(r'^home/', homepage_view, name="home"),
    url(r'^mensura/', include('apps.mensura.urls', namespace="mensura")),
    #url(r'^postulacion/', include('apps.postulacion.urls', namespace="postulacion")),
    #url(r'^renovacion/', include('apps.renovacion.urls', namespace="renovacion")),
    url(r'^prueba/', include('apps.prueba.urls', namespace="prueba")),
    url(r'^getProvincia/', getProvincia, name="obtener_provincia"),
    url(r'^getComuna/', getComuna, name="obtener_comuna"),
    url(r'^mis_datos/', editar_datos, name="editar_datos"),
    url(r'^reset_password/', reset_password, name="resetear_password"),
    url(r'^cambiar_password/', cambiar_password, name="cambiar_password"),
    url(r'^notas_generales/', notas_generales, name="notas_generales"),
    url(r'^notas_generales_det/(?P<rut>\d+)$', notas_generales_det, name="notas_generales_det"),
    url(r'^notas_generales_det2/(?P<rut>\d+)/(?P<periodo>\d+)$', notas_generales_det2, name="notas_generales_det2"),
    #url(r'^prueba_archivos/', descargaTodo, name="descarga_todo"),
    #url(r'^apelacion/', apelacion, name="apelacion"),
    #url(r'^responder_reclamacion/(?P<id>\d+)$', responde_reclamacion, name="responde_reclamacion"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
