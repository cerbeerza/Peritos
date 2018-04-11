from django.shortcuts import render
from apps.administration.models import User
from apps.renovacion.models import Renovacion
from datetime import date
from apps.periodo.models import PeriodoProceso




def renueva(request):

    if request.method == 'GET':


        return render(request, 'templates/renovacion/renovacion.html')

    if request.method == 'POST':

        userId = request.user.id
        idUsuarioFk = User.objects.get(id=userId)
        rutUser = idUsuarioFk.profile.rut



        #renovacion = Renovacion
        fecha_actual = date.today()
        objetoPeriodo = PeriodoProceso.objects.get(fechaDesde__lte=fecha_actual, fechaHasta__gte=fecha_actual)
        periodo = objetoPeriodo.periodo
        year = periodo[0:4]

        #renovacion.periodo = year
        #renovacion.fecha_creacion = fecha_actual
        #renovacion.doc_ci = ruta
        #renovacion.id_user_id = userId
        ruta = 'd:/files/ci/ci'+rutUser+'.pdf'
        ruta2 = 'd:/files/ant/ant'+rutUser+'.pdf'
        ruta3 = 'd:/files/tit/tit'+rutUser+'.pdf'
        handle_uploaded_file(request.FILES['fileCCI'], ruta)
        handle_uploaded_file(request.FILES['fileANT'], ruta2)
        handle_uploaded_file(request.FILES['fileTIT'], ruta3)
        renovacion = Renovacion.objects.create(periodo=year, fecha_creacion=fecha_actual, doc_ci=ruta, doc_ant=ruta2, doc_tit=ruta3, id_user_id=userId)




        return render(request, 'templates/renovacion/renovacion.html')





def handle_uploaded_file(f, ruta):
    with open(ruta, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

