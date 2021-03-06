from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
import requests, json
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from apps.administration.models import Profile

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

            periodos = requests.post("http://syspminweb-prod:8080/NotasPeritosREST/service/NotasPeritos/getPeriodos",
                                     data=datos, headers=cabeceras)
        except:
            estado = False
            message = "Ha ocurrido un problema para realizar tu consulta."
            return render(request, 'templates/mensura/mensura_general_list.html', {'listaPeriodos': None, 'estado': estado, 'message': message})




        listPeriodos = periodos.json()

        return render(request, 'templates/mensura/mensura_general_list.html', {'listaPeriodos': listPeriodos, 'estado':estado})


    elif request.method == "POST":

        usuario = request.user.id
        rutUsuario = Profile.objects.get(user_id=usuario)
        rutRut = rutUsuario.rut


        periodo = request.POST['selectPeriodo']

        cabeceras = {
            "Content-Type": "application/json"
        }

        datos = '{"periodo" : "'+periodo+'", "rutper" : "'+rutRut+'", "pass" : "sngmq21.,+"}'

        try:
            response = requests.post("http://syspminweb-prod:8080/NotasPeritosREST/service/NotasPeritos/getNotaPromedioByUser",
                                     data=datos, headers=cabeceras)
        except:
            message = "Ha ocurrido un problema para realizar tu consulta."
            estado = False
            return render(request, 'templates/mensura/mensura_general_list.html',
                          {'objeto2': None, 'listaPeriodos': None, 'estado':estado})

        datoJson = response.json()
        notaPromedio = datoJson['notaPromedio']
        movPer = datoJson['movPerito']
        empresa = datoJson['empresa']
        nombrePer = datoJson['nomper']
        situacion = None

        periodos = requests.post("http://syspminweb-prod:8080/NotasPeritosREST/service/NotasPeritos/getPeriodos",
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
def mensuraDetalleFn(request, periodo):

    if request.method == "GET":

        userId = request.user.id
        idUsuarioFk = User.objects.get(id=userId)
        rutUser = idUsuarioFk.profile.rut

        cabeceras = {
            "Content-Type": "application/json"
        }

        datos = '{ "periodo": "'+periodo+'", "rutper": "'+rutUser+'", "pass": "sngmq21.,+"}'

        notas = requests.post("http://syspminweb-prod:8080/NotasPeritosREST/service/NotasPeritos/getNotaParcialByUser", data=datos, headers=cabeceras)
        listadoNotas = notas.json()

        '''for listadoX in listadoNotas:

            fechaFull = listadoX['fecper']
            year = fechaFull[0:4]
            mes = fechaFull[5:7]
            dia = fechaFull[8:10]
            listadoX['fecper'] = dia + "/" + mes + "/" + year'''

        for indice in range(len(listadoNotas)):

            fechaFull = listadoNotas[indice]['fecper']
            year = fechaFull[0:4]
            mes = fechaFull[5:7]
            dia = fechaFull[8:10]
            listadoNotas[indice]['fecper'] = dia + "/" + mes + "/" + year


        return render(request, 'templates/mensura/mensura_general_list.html', {'objeto_detalle' : listadoNotas})









