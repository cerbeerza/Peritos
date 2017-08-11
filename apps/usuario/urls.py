from django.conf.urls import url, include

from apps.usuario.views import UsuarioList, UsuarioCreate, UsuarioUpdate, UsuarioDelete

urlpatterns = [
    
    url(r'^registrar$', UsuarioCreate.as_view(), name='usuario_crear'),
    url(r'^listar$', UsuarioList.as_view(), name='usuario_listar'),
    url(r'^editar/(?P<pk>\d+)/$', UsuarioUpdate.as_view(), name='usuario_editar'),
    url(r'^eliminar/(?P<pk>\d+)/$', UsuarioDelete.as_view(), name='usuario_eliminar'),
    
    
]