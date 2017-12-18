from django.template import RequestContext
from django.shortcuts import render
from Peritos.forms import LoginForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
#from apps.usuario.models import Usuario
from apps.administration.models import Profile
from apps.administration.forms import UserProfileForm, UserForm

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
                else:
                    message = "Inactivo"
            else:
                message = "Mal Password"

    else:
        form = LoginForm()
    return render(request, 'templates/administrations/login.html', {'message': message, 'form': form})

def registro_page(request):

    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST)
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
                profile.fecha_nac = request.POST['fecha_nac']
                profile.genero = request.POST['genero']
                profile.nacionalidad = request.POST['nacionalidad']
                profile.nombres = request.POST['nombres']
                profile.profesion = request.POST['profesion']
                profile.region = request.POST['region']
                profile.telefono_empresa  = request.POST['telefono_empresa']
                profile.universidad = request.POST['universidad']
                profile.year_titulo = request.POST['year_titulo']
                profile.rut = request.POST['rut']
                profile.save()

                message = 'Se ha creado el usuario'
            else: 'Usuario ya existe'
        else:
            message = 'Formulario no valido'

    else:
        user_form = UserForm
        profile_form = UserProfileForm

        message = None

    return render(request, 'templates/administrations/registroSimple.html', {'message': message, 'user_form': user_form, 'profile_form': profile_form})


















