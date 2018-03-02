from django.template import RequestContext, Context
from django.shortcuts import render, redirect
from Peritos.forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
#from apps.usuario.models import Usuario
from apps.administration.models import Profile
from apps.administration.forms import UserProfileForm, UserForm
from apps.zona.models import *
from django.http import HttpResponse
from django.http import JsonResponse


import datetime

from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

def login_page(request):
    message = None
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    message = "Correcto"
                    return render(request, 'templates/administrations/homepage.html')
                else:
                    message = "Inactivo"
            else:
                message = "Mal Password"

    else:
        form = LoginForm()
    return render(request, 'templates/administrations/login.html', {'message': message, 'form': form})

def registro_page(request):

    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, request.FILES)
        user_form = UserForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
        #if user_form.is_valid():
            try:
                var = User.objects.get(username=request.POST['username'])
            except ObjectDoesNotExist:
                var = None

            if var == None:

                user_form.save()

                #profile_form.save()
                user = User.objects.get(username=request.POST['username'])
                userId = user.id

                user.password = make_password(request.POST['password'], salt=None, hasher='default')
                user.save()



                profile = Profile.objects.get(user_id=userId)
                profile.direccion = request.POST['direccion']
                profile.telefono_cel = request.POST['telefono_cel']
                profile.telefono_casa = request.POST['telefono_casa']
                profile.apellido_p = request.POST['apellido_p']
                profile.apellido_m = request.POST['apellido_m']
                profile.comuna = request.POST['comuna']
                profile.direccion_empresa = request.POST['direccion_empresa']
                profile.empresa = request.POST['empresa']
                profile.estado_civil = request.POST['estado_civil']
                fechaNac = request.POST['fecha_nac']
                fechaFormat = datetime.datetime.strptime(fechaNac, '%d/%m/%Y')
                profile.fecha_nac = fechaFormat
                profile.genero = request.POST['genero']
                profile.nacionalidad = request.POST['nacionalidad']
                profile.nombres = request.POST['nombres']
                profile.profesion = request.POST['profesion']
                profile.region = request.POST['region']
                profile.telefono_empresa  = request.POST['telefono_empresa']
                profile.universidad = request.POST['universidad']
                profile.year_titulo = request.POST['year_titulo']
                profile.rut = request.POST['rut']

                handle_uploaded_file(request.FILES['archivo_titulo'])
                profile.save()

                message = 'Se ha creado el usuario'
            else: 'Usuario ya existe'
        else:
            message = 'Formulario no valido'

    else:
        user_form = UserForm
        profile_form = UserProfileForm

        message = None

    regiones = Region.objects.all()
    provincias = []
    comunas = []

    return render(request, 'templates/administrations/registro.html', {'message': message, 'user_form': user_form, 'profile_form': profile_form, 'regiones': regiones, 'provincias': provincias, 'comunas': comunas})


def handle_uploaded_file(f):
    with open('d:/files/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def getProvincia(request):

    nombre_region = request.GET['reg']

    result_set = []
    all_provincias = []

    answer = str(nombre_region[1:-1])
    selected_region = Region.objects.get(nombre=answer)

    all_provincias = selected_region.provincia_set.all()
    for provincia in all_provincias:
        result_set.append({'name': provincia.nombre})

    #return HttpResponse(json.dumps(result_set), content_type='application/json')
    return JsonResponse(result_set, safe=False)



def getComuna(request):

    nombre_provincia = request.GET['prov']

    result_set = []
    all_comunas = []

    answer = nombre_provincia
    selected_provincia = Provincia.objects.get(nombre=answer)

    all_comunas = selected_provincia.comuna_set.all()
    for comuna in all_comunas:
        result_set.append({'name': comuna.nombre})

    #return HttpResponse(json.dumps(result_set), content_type='application/json')
    return JsonResponse(result_set, safe=False)

def logout_view(request):
    logout(request)
    return redirect('/')

@login_required()
def homepage_view(request):
    return render(request, 'administrations/homepage.html')





















