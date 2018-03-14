from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
import requests, json
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from apps.mensura.models import MensuraGeneral


class Struct(object):
    def __init__(self, **entries):
        self.__dict__.update(entries)

class MensuraGeneralList(ListView):
    model = MensuraGeneral
    template_name = 'mensura/mensura_general_list.html'




@login_required()
def mensuraGeneralFn(request):



    estado = True
    if request.method == "GET":

        cabeceras = {
            "Content-Type": "application/json"
        }

        datos = '{ "pass": "sngmq21.,+"}'

        try:

            periodos = requests.post("http://172.16.61.214:8081/NotasPeritosREST/service/NotasPeritos/getPeriodos",
                                     data=datos, headers=cabeceras)
        except:
            estado = False
            message = "Ha ocurrido un problema para realizar tu consulta, no necesitas saber por que"
            return render(request, 'templates/mensura/mensura_general_list.html', {'listaPeriodos': None, 'estado': estado, 'message': message})




        listPeriodos = periodos.json()

        return render(request, 'templates/mensura/mensura_general_list.html', {'listaPeriodos' : listPeriodos, 'estado': estado})


    elif request.method == "POST":


        periodo = request.POST['selectPeriodo']

        cabeceras = {
            "Content-Type": "application/json"
        }

        datos = '{"periodo" : "'+periodo+'", "rutper" : "008050812", "pass" : "sngmq21.,+"}'

        try:
            response = requests.post("http://172.16.61.214:8081/NotasPeritosREST/service/NotasPeritos/getNotaPromedioByUser",
                                     data=datos, headers=cabeceras)
        except:
            message = "Ha ocurrido un problema para realizar tu consulta, no necesitas saber por que"
            estado = False
            return render(request, 'templates/mensura/mensura_general_list.html',
                          {'objeto2': None, 'listaPeriodos': None, 'estado':estado})

        datoJson = response.json()
        notaPromedio = datoJson['notaPromedio']
        movPer = datoJson['movPerito']
        empresa = datoJson['empresa']
        nombrePer = datoJson['nomper']
        situacion = None

        periodos = requests.post("http://172.16.61.214:8081/NotasPeritosREST/service/NotasPeritos/getPeriodos",
                                 data=datos, headers=cabeceras)

        listPeriodos = periodos.json()

        if notaPromedio is not None:

            if float(notaPromedio) < 4:
                situacion = "Reprobado"
            else:
                situacion = "Aprobado"

        else:
            return render(request, 'templates/mensura/mensura_general_list.html', {'objeto2': None, 'listaPeriodos' : listPeriodos, 'estado': estado})



        objeto = {"notaPromedio": notaPromedio, "movPer": movPer, "periodo": periodo, "empresa": empresa, "nombrePer" : nombrePer, "situacion" : situacion}

        objeto2 = Struct(**objeto)


        return render(request, 'templates/mensura/mensura_general_list.html', {'objeto2' : objeto2, 'listaPeriodos' : listPeriodos, 'estado': estado})


@login_required()
def mensuraDetalleFn(request):

    if request.method == "GET":

        userId = request.user.id
        idUsuarioFk = User.objects.get(id=userId)
        rutUser = idUsuarioFk.profile.rut

        return render(request, 'templates/mensura/mensura_general_list.html',)









