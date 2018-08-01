from django.shortcuts import render
from datetime import date
from apps.periodo.models import PeriodoProceso
from apps.apelacion.models import Apelacion
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from apps.administration.models import Profile
from apps.postulacion.models import Postulacion
from apps.prueba.models import Prueba

def apelacion(request):

    if request.method == 'GET':


        profile = Profile.objects.get(user_id=request.user.id)
        renueva = profile.renovante

        return render(request, 'templates/apelacion/apelacion.html',{'renovante': renueva})

    if request.method == 'POST':

        fecha_actual = date.today()
        objetoPeriodo = PeriodoProceso.objects.get(fechaDesde__lte=fecha_actual, fechaHasta__gte=fecha_actual)
        periodo = objetoPeriodo.periodo
        year = periodo[0:4]
        apelacionDesc = request.POST['txtApelacion']
        userId = request.user.id
        idUsuarioFk = User.objects.get(id=userId)
        profile = Profile.objects.get(user_id=userId)
        if len(Postulacion.objects.filter(periodo='2017', id_user_id=userId)) > 0 and len(Prueba.objects.filter(rutx=profile.rut, periodo='2018')) > 0:

            postulacion = Postulacion.objects.get(id_user_id=userId, periodo='2017')

            prueba = Prueba.objects.get(rutx=profile.rut, periodo='2018')

            message = 'Se ha realizado correctamente su Reclamación, recibirá un correo electrónico con información sobre su respuesta'

            mensaje_email = EmailMessage(subject='Reclamación Proceso Peritos',
                                         body='Estimado/a ' + profile.nombres + ' ' + profile.apellido_p + ' Su reclamación ha sido registrada satisfactoriamente, y prontamente nos contactaremos con usted al correo ' + idUsuarioFk.email + ' para fijar una reunión en donde se le mostrará la corrección de su examen. Saludos.',
                                         from_email='procesoperitos@sernageomin.cl',
                                         to=[idUsuarioFk.email],
                                         )
            mensaje_email.send()

            mensaje_email2 = EmailMessage(subject='Información de Reclamación',
                                          body='El siguiente sujeto ha apelado: ' + profile.nombres + ' ' + profile.apellido_p + ' Rut: ' + profile.rut + ' Región Exámen: ' + postulacion.region_examen + ' Nota Prueba: ' + prueba.nota,
                                          from_email='procesoperitos@sernageomin.cl',
                                          to=['rodrigo.urrutia@sernageomin.cl', 'msoledad.cortes@sernageomin.cl'],
                                          )

            mensaje_email2.send()

            Apelacion.objects.create(periodo=year, desc_apelacion=apelacionDesc, usuario_id=userId)


            return render(request, 'templates/administrations/homepage.html', {'message': message})
        else:

            message = 'No posee los datos necesarios para realizar su reclamación'
            return render(request, 'templates/administrations/homepage.html', {'message': message})



