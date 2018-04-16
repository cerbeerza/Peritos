from django.shortcuts import render
from datetime import date
from apps.periodo.models import PeriodoProceso
from apps.apelacion.models import Apelacion
from django.contrib.auth.models import User

def apelacion(request):

    if request.method == 'GET':

        return render(request, 'templates/apelacion/apelacion.html')

    if request.method == 'POST':

        fecha_actual = date.today()
        objetoPeriodo = PeriodoProceso.objects.get(fechaDesde__lte=fecha_actual, fechaHasta__gte=fecha_actual)
        periodo = objetoPeriodo.periodo
        year = periodo[0:4]
        apelacionDesc = request.POST['txtApelacion']
        userId = request.user.id
        idUsuarioFk = User.objects.get(id=userId)
        message = 'Se ha realizado su Apelación'

        Apelacion.objects.create(periodo=year, desc_apelacion=apelacionDesc, usuario_id=userId)
        return render(request, 'templates/apelacion/apelacion.html', {'message': message})



