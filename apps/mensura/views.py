from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
import requests, json

from apps.mensura.models import MensuraGeneral


class MensuraGeneralList(ListView):
    model = MensuraGeneral
    template_name = 'mensura/mensura_general_list.html'

def mensuraGeneralFn(request):

    if request.method == "GET":

        return render(request, 'templates/mensura/mensura_general_list.html', {'objeto' : None})

    elif request.method == "POST":

        periodo = request.POST['selectPeriodo']

        cabeceras = {
            "Content-Type": "application/json"
        }

        datos = '{"periodo" : "'+periodo+'", "rutper" : "008050812", "pass" : "sngmq21.,+"}'
        response = requests.post("http://172.16.61.214:8081/NotasPeritosREST/service/NotasPeritos/getNotaPromedioByUser",
                                 data=datos, headers=cabeceras)
        datoJson = response.json()
        notaPromedio = datoJson['notaPromedio']
        movPer = datoJson['movPerito']


        objeto = {"notaPromedio": notaPromedio, "movPer": movPer, "periodo": periodo}

        return render(request, 'templates/mensura/mensura_general_list.html', {'objeto' : objeto})



