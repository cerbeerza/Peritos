from django.shortcuts import render
from apps.postulacion.forms import PostulacionForm
from apps.zona.models import Region
from apps.postulacion.models import Postulacion
from django.contrib.auth.models import User
from datetime import date
from django.contrib.auth.decorators import login_required

@login_required()
def crea_postulacion(request):
    message = None
    regiones = []
    if request.method == "POST":
        form = PostulacionForm(request.POST)
        if form.is_valid():

            fechaActual = date.today()
            yearPeriodo = fechaActual.year
            region = request.POST['region_examen']
            userId = request.user.id
            idUsuarioFk = User.objects.get(id=userId)
            registroPost = Postulacion.objects.filter(id_user_id=userId)
            if len(registroPost) != 0:
                message = "Ya ha realizado una postulación para este periodo"
                regiones = Region.objects.all()
                form = PostulacionForm
                return render(request, 'templates/postulacion/postulacion_create.html',
                              {'form': form, 'regiones': regiones, 'message': message})

            postulacion = Postulacion(id_user=idUsuarioFk, region_examen=region, periodo=yearPeriodo)
            postulacion.save()

            message = "Se ha realizado su postulación correctamente"
            return render(request, 'templates/administrations/homepage.html', {'message': message})
    else:
        form = PostulacionForm
        regiones = Region.objects.all()



    return render(request, 'templates/postulacion/postulacion_create.html', {'form': form, 'regiones': regiones})


