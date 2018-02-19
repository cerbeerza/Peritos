from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from apps.prueba.views import PruebaList

urlpatterns = [

    url(r'^listar$', login_required(PruebaList.as_view()), name='prueba_listar'),
]

