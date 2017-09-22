from django.template import RequestContext
from django.shortcuts import render
from Peritos.forms import LoginForm
from django.contrib.auth import authenticate, login
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

            '''    
            try:
                usuario = Usuario.objects.get(rut=username)
            except ObjectDoesNotExist:
                usuario = None
                message = "Usuario no existe"

            if usuario is not None:
                if usuario.password == password:
                    #login(request, usuario)
                    message= "Correcto"
                else:
                    message= "Password Incorrecto"
                    '''
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
    '''message = None
    if request.method == "POST":
        rut = request.POST['']

        try:
            var = Profile.objects.get(rut=rut)
        except ObjectDoesNotExist:
            var = None

        if var == None:
            # Recojer todos los datos necesarios
            direccion = request.POST['']
            apellidoM = request.POST['']
            appelidoP = request.POST['']
            comuna = request.POST['']
            direccionEmpresa = request.POST['']
            empresa = request.POST['']
            estadoCivil = request.POST['']
            fechaNac = request.POST['']
            genero = request.POST['']
            nacionalidad = request.POST['']
            nombres = request.POST['']
            profesion = request.POST['']
            region = request.POST['']
            telefonoCasa = request.POST['']
            telefonoEmpresa = request.POST['']
            universidad = request.POST['']
            yearTitulo = request.POST['']
            telefonoCel = request.POST['']
            password = request.POST['']


            User.password = password
            User.is_superuser = False
            User.first_name = nombres '''

    #message = 'ALGO'
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST)
        user_form = UserForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            try:
                var = User.objects.get(username=request.POST['username'])
            except ObjectDoesNotExist:
                var = None

            if var == None:
                #usuario = User.objects.create(username = request.POST['username'], email = request.POST['email'], password = request.POST['password'])
                #usuario.save()
                #usuarioActual = User.objects.get(username=request.POST['username'])
                #p = Profile.objects.get(user_id=usuarioActual.id)
                #p.apellido_p = request.POST['apellido_p']
                #p.save()
                user_form.save()

                profile_form.save()
                #profile_form.save()


                message = 'Se ha creado el usuario'
            else: 'Usuario ya existe'
        else:
            message = 'Formulario no valido'

    else:
        user_form = UserForm
        profile_form = UserProfileForm


        message = None

    return render(request, 'templates/administrations/registroSimple.html', {'message': message, 'user_form': user_form, 'profile_form': profile_form})


















