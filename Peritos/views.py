from django.template import RequestContext
from django.shortcuts import render
from Peritos.forms import LoginForm
from django.contrib.auth import authenticate, login

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
                    message= "Correcto"
                else:
                    message= "Usuario Inactivo"
            else:
                message = "Nombre o Password Incorrecto"
    else:
        form = LoginForm()
    return render(request ,'login.html', {'message': message, 'form': form})



