from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from apps.prueba.views import PruebaList, pruebaListFn

urlpatterns = [

    url(r'^listar$', login_required(PruebaList.as_view()), name='prueba_listar'),
    #url(r'^listar2$', pruebaListFn, name='prueba_listar'),
]

