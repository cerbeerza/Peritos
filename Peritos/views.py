from django.template import RequestContext
from django.shortcuts import render
from Peritos.forms import LoginForm
from django.contrib.auth import authenticate, login
#from apps.usuario.models import Usuario
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
    message = None
    if request.method == "POST":




