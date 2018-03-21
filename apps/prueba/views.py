from django.shortcuts import render
from django.views.generic import ListView
from apps.prueba.models import Prueba
from apps.administration.models import Profile
from django.contrib.auth.decorators import login_required
import requests, json





class PruebaList(ListView):

    model = Prueba
    queryset = Prueba.objects.filter(periodo='2016')
    template_name = 'prueba/prueba_list.html'

@login_required()
def pruebaListFn(request):



    resultado = None

    if request.user.is_authenticated():
        userId = request.user.id
        getUser = Profile.objects.get(id=userId)
        userRut = getUser.rut
        resultado = Prueba.objects.filter(rutx=userRut)

    return render(request, 'templates/prueba/prueba_list.html', {'objeto': resultado})










