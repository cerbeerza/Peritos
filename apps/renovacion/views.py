from django.shortcuts import render
from apps.administration.models import User
from apps.renovacion.models import Renovacion
from datetime import date
from apps.periodo.models import PeriodoProceso
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from apps.administration.models import Profile
from django.contrib.auth.decorators import login_required


@login_required()
def renueva(request):

    if request.method == 'GET':

        userId = request.user.id
        profile = Profile.objects.get(user_id=userId)
        renueva = profile.renovante

        return render(request, 'templates/renovacion/renovacion.html', {'renueva': renueva})

    if request.method == 'POST':

        userId = request.user.id
        idUsuarioFk = User.objects.get(id=userId)
        rutUser = idUsuarioFk.profile.rut




        #renovacion = Renovacion
        fecha_actual = date.today()
        objetoPeriodo = PeriodoProceso.objects.get(fechaDesde__lte=fecha_actual, fechaHasta__gte=fecha_actual)
        periodo = objetoPeriodo.periodo
        year = periodo[0:4]

        renovaciones = Renovacion.objects.filter(id_user_id=userId, periodo=year)
        if len(renovaciones) != 0:
            message =  'Ya ha realizado renovación para este periodo'
            return render(request, 'templates/renovacion/renovacion.html', {'message': message})


        renovacion = Renovacion.objects.create(periodo=year, fecha_creacion=fecha_actual, id_user_id=userId, archivo_ci=request.FILES['fileCCI'], archivo_ant=request.FILES['fileANT'], archivo_tit=request.FILES['fileTIT'])




        mensaje_email = EmailMessage(subject='Renovación Proceso Peritos',
                                     body='Se ha Realizado correctamente su Renovación',
                                     from_email='procesoperitos@sernageomin.cl',
                                     to=[idUsuarioFk.email],
                                     )
        mensaje_email.send()

        message = "Se ha realizado correctamente su Renovación"

        renueva = True

        return render(request, 'templates/renovacion/renovacion.html', {'message': message, 'renueva': renueva})






def handle_uploaded_file(f):
    with open('default', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

