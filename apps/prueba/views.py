from django.shortcuts import render
from django.views.generic import ListView
from apps.prueba.models import Prueba
from apps.administration.models import Profile
import requests, json





class PruebaList(ListView):

    model = Prueba
    queryset = Prueba.objects.filter(periodo='2016')
    template_name = 'prueba/prueba_list.html'


def pruebaListFn(request):


    cabeceras = {
        "Content-Type": "application/json"
    }

    datos = '{"periodo" : "2011", "rutper" : "008050812", "pass" : "sngmq21.,+"}'
    response = requests.post("http://172.16.61.214:8081/NotasPeritosREST/service/NotasPeritos/getNotaPromedioByUser", data=datos, headers = cabeceras)
    datoJson = response.json()
    notaPromedio = datoJson['notaPromedio']
    movPer = datoJson['movPerito']
    periodo = datoJson['periodo']
    resultado = None

    if request.user.is_authenticated():
        userId = request.user.id
        getUser = Profile.objects.get(id=userId)
        userRut = getUser.rut
        resultado = Prueba.objects.filter(rut=userRut)



    return render(request, 'templates/prueba/prueba_list.html',{'objeto': resultado})

