from django.conf.urls import url, include

from apps.mensura.views import MensuraGeneralList, mensuraGeneralFn

urlpatterns = [

    #url(r'^registrar$', MensuraGeneralCreate.as_view(), name='mensura_general_crear'),
    url(r'^listar$', mensuraGeneralFn, name='mensura_general_listar'),

]