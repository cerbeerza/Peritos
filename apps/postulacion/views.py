from django.shortcuts import render
from apps.postulacion.forms import PostulacionForm
from apps.zona.models import Region
from apps.postulacion.models import Postulacion
from django.contrib.auth.models import User
from datetime import date

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
            postulacion = Postulacion(id_user=idUsuarioFk, region_examen=region, periodo=yearPeriodo)
            postulacion.save()

            message = "Se ha realizado su postulación correctamente"
            return render(request, 'templates/administrations/homepage.html', {'message': message})
    else:
        form = PostulacionForm
        regiones = Region.objects.all()



    return render(request, 'templates/postulacion/postulacion_create.html', {'form': form, 'regiones': regiones})


