from django.conf.urls import url, include

from apps.mensura.views import MensuraGeneralList, mensuraGeneralFn, mensuraDetalleFn

urlpatterns = [

    #url(r'^registrar$', MensuraGeneralCreate.as_view(), name='mensura_general_crear'),
    url(r'^listar$', mensuraGeneralFn, name='mensura_general_listar'),
    url(r'^detalle_mensura$', mensuraDetalleFn, name='mensura_detalle_listar'),


]