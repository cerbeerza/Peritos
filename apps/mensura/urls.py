from django.conf.urls import url, include

from apps.mensura.views import MensuraGeneralList, MensuraGeneralCreate, MensuraGeneralUpdate, MensuraGeneralDelete

urlpatterns = [
    
    url(r'^registrar$', MensuraGeneralCreate.as_view(), name='mensura_general_crear'),
    url(r'^listar$', MensuraGeneralList.as_view(), name='mensura_general_listar'),
    url(r'^editar/(?P<pk>\d+)/$', MensuraGeneralUpdate.as_view(), name='mensura_general_editar'),
    url(r'^eliminar/(?P<pk>\d+)/$', MensuraGeneralDelete.as_view(), name='mensura_general_eliminar'),
    
    
]