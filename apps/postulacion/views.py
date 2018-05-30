from django.shortcuts import render
from apps.postulacion.forms import PostulacionForm
from apps.zona.models import Region
from apps.administration.models import Profile
from apps.postulacion.models import Postulacion
from django.contrib.auth.models import User
from datetime import date
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from apps.periodo.models import PeriodoProceso

@login_required()
def crea_postulacion(request):
    message = None
    regiones = []
    if request.method == "POST":
        form = PostulacionForm(request.POST)
        if form.is_valid():

            #fechaActual = date.today()
            #yearPeriodo = fechaActual.year
            fecha_actual = date.today()
            objetoPeriodo = PeriodoProceso.objects.get(fechaDesde__lte=fecha_actual, fechaHasta__gte=fecha_actual)
            periodo = objetoPeriodo.periodo
            year = periodo[0:4]
            region = request.POST['region_examen']
            userId = request.user.id
            idUsuarioFk = User.objects.get(id=userId)
            registroPost = Postulacion.objects.filter(id_user_id=userId, periodo=year)

            if len(registroPost) != 0:
                message = "Ya ha realizado una postulación para este periodo"
                regiones = Region.objects.all()
                form = PostulacionForm
                return render(request, 'templates/postulacion/postulacion_create.html',
                              {'form': form, 'regiones': regiones, 'message': message})

            postulacion = Postulacion(id_user=idUsuarioFk, region_examen=region, periodo=year)
            postulacion.save()

            message = "Se ha realizado su postulación correctamente"


            mensaje_email = EmailMessage(subject='Postulación Proceso Peritos',
                                         body='Se ha Realizado correctamente su Postulación',
                                         from_email='procesoperitos@sernageomin.cl',
                                         to=[idUsuarioFk.email],
                                         )
            mensaje_email.send()


            return render(request, 'templates/administrations/homepage.html', {'message': message})
    else:
        form = PostulacionForm
        regiones = Region.objects.all()



    return render(request, 'templates/postulacion/postulacion_create.html', {'form': form, 'regiones': regiones})


