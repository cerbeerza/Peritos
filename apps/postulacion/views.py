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
    # Arreglo
    renueva = None
    finalizado = False

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
            finalizado = True


            mensaje_email = EmailMessage(subject='Postulación Proceso Peritos',
                                         body='Se ha Realizado correctamente su Postulación, por lo tanto debe rendir el exámen el día 02 de Agosto a las 09:00 Horas. Si usted rinde el examen en Santiago, debe dirigirse al auditorio de Sta María 0180, y, si desea rendir el exámen en regiones, debe dirigirse a la dirección Regional correspondiente. No olvide que debe presentar la siguiente documentación el día del examen: Título original o copia legalizada ante notario, Certificado de Antecedentes, Copia C.I en ambos lados.',
                                         from_email='procesoperitos@sernageomin.cl',
                                         to=[idUsuarioFk.email],
                                         cc=('procesoperitos@sernageomin.cl',),
                                         )
            #mensaje_email.send()


            return render(request, 'templates/administrations/homepage.html', {'message': message, 'finalizado': finalizado})
    else:
        form = PostulacionForm
        regiones = Region.objects.all()

        userId = request.user.id
        profile = Profile.objects.get(user_id=userId)
        renueva = profile.renovante



    return render(request, 'templates/postulacion/postulacion_create.html', {'form': form, 'regiones': regiones, 'renueva': renueva})


