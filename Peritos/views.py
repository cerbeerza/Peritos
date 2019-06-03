from django.template import RequestContext, Context
from django.shortcuts import render, redirect
from Peritos.forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
#from apps.usuario.models import Usuario
from apps.administration.models import Profile
from apps.administration.forms import UserProfileForm, UserForm, UserEditForm
from apps.zona.models import *
from django.http import HttpResponse
from django.http import JsonResponse
from random import choice
from django.core.mail import EmailMessage
from apps.nomina.models import Nomina
from datetime import date
from apps.periodo.models import PeriodoProceso
import requests, json
from apps.prueba.models import Prueba
from PyPDF2 import PdfFileWriter, PdfFileReader
from django.db.models import Max
from apps.apelacion.models import Apelacion




import datetime

from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

def login_page(request):
    message = None
    message2 = None
    message3 = None
    verificaNota = False
    calculaNota = False
    if request.method == "POST":

        '''
        #bloque para cambio de password cifrada
        listaQuerySet = User.objects.all()
        for elemento in listaQuerySet:
            idElemento = elemento.id
            objetoUser = User.objects.get(id=idElemento)
            passwordNativa = objetoUser.password
            objetoUser.password = make_password(passwordNativa)
            objetoUser.save()

        message = "OK" '''

        form = LoginForm(request.POST)
        if form.is_valid():
            rutOriginal = request.POST['username']
            largo = len(rutOriginal)
            rutFormateado = rutOriginal[0: largo - 2]
            rutFinal = rutFormateado.replace('.', '')
            username = rutFinal
            password = request.POST['password']

            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    message = "Correcto"



                    #Validación de Tipo de Usuario
                    fecha_actual = date.today()
                    objetoPeriodo = PeriodoProceso.objects.get(fechaDesde__lte=fecha_actual,
                                                               fechaHasta__gte=fecha_actual)
                    periodo = objetoPeriodo.periodo
                    year = periodo[0:4]
                    year2 = int(year) - 1

                    usuario = request.user.id
                    rutUsuario = Profile.objects.get(user_id=usuario)
                    rutRut = rutUsuario.rut
                    '''
                    nomina = Nomina.objects.filter(rut_nomina=rutUsuario.rut, periodo=year)

                    if len(nomina) == 0:
                        message = 'Según nuestros registros usted no aparece en como NOMINADO, usted debe postular'
                        rutUsuario.renovante = False
                        rutUsuario.save()


                    else:
                        message = 'Usted aparece en nuestros Registros como NOMINADO, usted debe renovar'
                        verificaNota = True
                        rutUsuario.renovante = True
                        rutUsuario.save()


                        #si es SNGM
                        if rutUsuario.sngm:
                            verificaNota = False
                            rutUsuario.renovante = True
                            rutUsuario.save()

                        #si dio prueba recientemente
                        contExamen = Prueba.objects.filter(rutx=rutRut, periodo=year, situacion='APROBADO')

                        if len(contExamen) > 0:
                            verificaNota = False
                            rutUsuario.renovante = True
                            rutUsuario.save()


                    if verificaNota:

                        #Validación de Periodos o Notas
                        cabeceras = {
                            "Content-Type": "application/json"
                        }

                        datos = '{ "periodo": "' + str(year2+2) + '", "rutper": "'+rutRut+'", "pass": "sngmq21.,+"}'

                        notas = requests.post(
                            "http://syspminweb-prod:8080/NotasPeritosREST/service/NotasPeritos/getNotaParcialByUser",
                            data=datos, headers=cabeceras)
                        listadoNotas = notas.json()

                        if len(listadoNotas) == 0:

                            datos = '{ "periodo": "' + str(year2+1) + '", "rutper": "'+rutRut+'", "pass": "sngmq21.,+"}'
                            notas = requests.post(
                                "http://syspminweb-prod:8080/NotasPeritosREST/service/NotasPeritos/getNotaParcialByUser",
                                data=datos, headers=cabeceras)
                            listadoNotas = notas.json()

                            if len(listadoNotas) == 0:
                                message2 = 'No presenta notas de mensuras en 2 periodos, no puede renovar'
                                message = None
                                #nuevo
                                rutUsuario.renovante = False
                                rutUsuario.save()
                            else:
                                calculaNota = True
                        else:
                            calculaNota = True

                        if calculaNota:
                            suma = 0.0
                            for indice in range(len(listadoNotas)):

                                notaParcial = float(listadoNotas[indice]['notaParcial'])
                                suma = suma + notaParcial
                            total = suma / len(listadoNotas)

                            message3 = 'Su nota promedio actual para este periodo es ' + str(round(total,1))
                            if total < 4.0:
                                message2 = 'Hasta el momento su nota es inferior a 4.0, lo que significa que por el momento no puede renovar'
                                rutUsuario.renovante = False
                                rutUsuario.save()
                            elif total == 0.0:
                                message2 = 'No presenta notas'
                                rutUsuario.renovante = False
                                rutUsuario.save()
                                '''


                    objUsuario = Profile.objects.get(rut=rutRut)
                    nombreUsuario = objUsuario.nombres
                    apellidoUsuario = objUsuario.apellido_p
                    return render(request, 'templates/administrations/homepage.html', {'message': message, 'message2' : message2,'message3': message3, 'nombres': nombreUsuario, 'ape1': apellidoUsuario})
                    #return render(request, 'templates/renovacion/ficha.html')
                else:
                    message = "Inactivo"
            else:
                message = "Mal Password"

    else:
        form = LoginForm()
    return render(request, 'templates/administrations/login.html', {'message': message, 'form': form})


@login_required()
def responde_reclamacion(request, id):

    if request.method == 'GET' and request.user.is_superuser:

        return render(request, 'templates/administrations/responde_reclamacion.html')

    if request.method == 'POST' and request.user.is_superuser:

        detalleMsg = request.POST['txtApelacion']
        apelacion = Apelacion.objects.get(id=id)
        apelacion.respuesta = detalleMsg
        apelacion.save()
        usuario = User.objects.get(id=apelacion.usuario_id)



        mensaje_email = EmailMessage(subject='Respuesta Reclamación',
                                     body='Estimado/a, su reclamación ha sido respondida con el siguiente mensaje: ' + detalleMsg,
                                     from_email='procesoperitos@sernageomin.cl',
                                     to=[usuario.email],
                                     cc=['procesoperitos@sernageomin.cl']
                                     )
        mensaje_email.send()

        message = "La reclamación ha sido respondida correctamente"


        return render(request, 'templates/administrations/responde_reclamacion.html', {'message_reclama': message})







@login_required()
def notas_generales(request):

    if request.method == 'GET' and request.user.is_superuser:


        fecha_actual = date.today()
        year = fecha_actual.year
        periodo = year - 1
        objetoPeriodo = PeriodoProceso.objects.get(fechaDesde__lte=fecha_actual,
                                                   fechaHasta__gte=fecha_actual)
        soloPeriodo = objetoPeriodo.periodo
        substr = soloPeriodo[0:4]
        numericPeriodo = int(substr)
        periodoFinal = numericPeriodo - 1

        #qs_profiles = Profile.objects.filter(renovante=True).order_by('nombres')
        qs_profiles = Profile.objects.raw('SELECT pf.id as id, pf.nombres as nombres, pf.apellido_p as apellido_p, pf.apellido_m as apellido_m, pf.rut as rut from administration_profile pf, nomina_nomina nm where pf.rut = nm.rut_nomina and nm.periodo = "'+ str(periodoFinal) +'" order by pf.nombres ')
        return render(request, 'templates/administrations/notas_generales.html', {'qs_profiles': qs_profiles})


@login_required()
def notas_generales_det(request, rut):

    if request.method == 'GET' and request.user.is_superuser:

        cabeceras = {
            "Content-Type": "application/json"
        }

        datos = '{ "rutper": "' + rut + '", "pass": "sngmq21.,+"}'

        notas = requests.post(
            "http://syspminweb-prod:8080/NotasPeritosREST/service/NotasPeritos/getNotasGenerales",
            data=datos, headers=cabeceras)
        listadoNotas = notas.json()


        return render(request, 'templates/administrations/notas_generales_det.html', {'listadoNotas': listadoNotas, 'rut': rut})

@login_required()
def notas_generales_det2(request, rut, periodo):

    if request.method == 'GET' and request.user.is_superuser:

        cabeceras = {
            "Content-Type": "application/json"
        }

        datos = '{ "rutper": "' + rut + '", "periodo": "'+ periodo +'", "pass": "sngmq21.,+"}'

        notas = requests.post(
            "http://syspminweb-prod:8080/NotasPeritosREST/service/NotasPeritos/getNotaParcialByUser",
            data=datos, headers=cabeceras)
        listadoNotas = notas.json()

        return render(request, 'templates/administrations/notas_generales_det2.html', {'listadoNotas': listadoNotas, 'rut': rut})






def registro_page(request):

    if request.method == 'POST':
        registrado = False
        profile_form = UserProfileForm(request.POST, request.FILES)
        user_form = UserForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
        #if user_form.is_valid():
            rutOriginal = request.POST['rut']
            largo = len(rutOriginal)
            rutFormateado = rutOriginal[0: largo - 2]
            rutFinal = rutFormateado.replace('.', '')

            try:
                #var = User.objects.get(rutFinal)
                var = Profile.objects.get(rut=rutFinal)
            except ObjectDoesNotExist:

                var = None

            if var is None:

                pass2 = request.POST['txtPass2']
                pass1 = request.POST['password']
                if pass1 != pass2:
                    message = 'Las contraseñas no coinciden'
                    return render(request, 'templates/administrations/registro.html',{'message': message, 'user_form': user_form, 'profile_form': profile_form})

                #Cambio por sacado de username
                #user_form.save()
                User.objects.create(username=rutFinal, password=request.POST['password'], email=request.POST['email'], first_name=request.POST['nombres'], last_name=request.POST['apellido_p'] )


                #profile_form.save()
                user = User.objects.get(username=rutFinal)
                userId = user.id
                user.password = make_password(pass1, salt=None, hasher='default')
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
                #rutFormateado = request.POST['rut']
                #rutFormateado = rutFormateado[0: len(rutFormateado) - 2]
                #rutFormateado = rutFormateado.replace('.', '')
                profile.rut = rutFinal
                profile.provincia = request.POST['provincia']

                #handle_uploaded_file(request.FILES['archivo_titulo'])
                profile.save()

                message = 'Se ha creado el usuario'

                form = LoginForm()

                correo = request.POST['email']

                mensaje_email = EmailMessage(subject='Registro de Usuario Plataforma Peritos',
                                             body='Se ha registrado correctamente a nuestra plataforma para Proceso de Postulación y Renovación de Peritos Mensuradores',
                                             from_email='procesoperitos@sernageomin.cl',
                                             to=[correo],
                                             )
                mensaje_email.send()

                #return render(request, 'templates/administrations/login.html', {'message': message, 'form' : form})
                return render(request, 'templates/administrations/registro.html', {'registrado' : True, 'message' : message})
                #return redirect('/')

            else:
                message = 'Usuario ya existe'
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



def reset_password(request):

    if request.method == 'GET':
        return render(request, 'templates/administrations/reset_password.html')

    if request.method == 'POST':
        rutUsuario = request.POST['rut_input']
        rutFormat = rutUsuario[0:len(rutUsuario)-2]
        rutFormat = rutFormat.replace(".","")
        profile = Profile.objects.get(rut=rutFormat)
        usuario = User.objects.get(id=profile.user_id)
        longitud = 10
        valores = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        p = ""
        p = p.join([choice(valores) for i in range(longitud)])
        pc = make_password(p, salt=None, hasher='default')
        usuario.password = pc
        usuario.save()
        correo = usuario.email
        volver = False


        mensaje_email = EmailMessage(subject='Reseteo de Password',
                                     body='Estimado, usuario, su contraseña ha sido reestablecida, su contraseña ahora es: '+ p + '  Recuerde que puede cambiarla desde el menú una vez iniciada la sesión.',
                                     from_email='procesoperitos@sernageomin.cl',
                                     to=[correo],
                                     )
        mensaje_email.send()

        message = "Mensaje Enviado a su correo electrónico"
        volver = True



        return render(request, 'templates/administrations/reset_password.html', { 'message' : message, 'volver': volver})


@login_required()
def cambiar_password(request):

    if request.method == 'GET':
        return render(request, 'templates/administrations/cambia_password.html')

    if request.method == 'POST':

        message = None
        volver = False
        usuario = request.user.id
        pass1 = request.POST['pass1_input']
        pass2 = request.POST['pass2_input']

        if pass1 != pass2:
            message = 'Las contraseñas deben ser iguales'

        else:

            objetoUser = User.objects.get(id=usuario)
            hashPass = make_password(pass1, salt=None, hasher='default')
            objetoUser.password = hashPass
            objetoUser.save()
            message = 'Su contraseña ha sido actualizada'
            volver = True


        return render(request, 'templates/administrations/cambia_password.html', { 'message' : message, 'volver': volver})





@login_required()
def editar_datos(request):

    if request.method == "GET":

        userId = request.user.id
        idUsuarioFk = User.objects.get(id=userId)
        rutUser = idUsuarioFk.profile.rut
        datos_personales = Profile.objects.get(rut=rutUser)

        datos = {
                 'nombres': datos_personales.nombres,
                 'apellido_p': datos_personales.apellido_p,
                 'apellido_m': datos_personales.apellido_m,
                 'fecha_nac': datos_personales.fecha_nac,
                 #'rut': datos_personales.rut,
                 'genero': datos_personales.genero,
                 'nacionalidad': datos_personales.nacionalidad,
                 'direccion': datos_personales.direccion,
                 'region': datos_personales.region,
                 'comuna': datos_personales.comuna,
                 'estado_civil': datos_personales.estado_civil,
                 'telefono_casa': datos_personales.telefono_casa,
                 'telefono_cel': datos_personales.telefono_cel,
                 'profesion': datos_personales.profesion,
                 'universidad': datos_personales.universidad,
                 'year_titulo': datos_personales.year_titulo,
                 'empresa': datos_personales.empresa,
                 'telefono_empresa': datos_personales.telefono_empresa,
                 'direccion_empresa': datos_personales.direccion_empresa,
                 'provincia': datos_personales.provincia,

                }

        datosUser = {
                        'email': idUsuarioFk.email,
                        'username': idUsuarioFk.username,
                    }

        profile_form = UserEditForm(initial=datos)
        user_form = UserForm(initial=datosUser)

        regiones = Region.objects.all()
        provincias = []
        comunas = []

        return render(request, 'administrations/editar_datos.html', { 'profile_form' : profile_form, 'user_form': user_form, 'regiones': regiones, 'provincias': provincias, 'comunas': comunas, 'datosPersonales': datos_personales})

    if request.method == "POST":

        form = UserEditForm(request.POST)
        if form.is_valid():

            userId = request.user.id
            usuario = User.objects.get(id=userId)
            profile = Profile.objects.get(user_id=usuario)
            profile.nombres = request.POST['nombres']
            profile.apellido_p = request.POST['apellido_p']
            profile.apellido_m = request.POST['apellido_m']
            fecha_nac = request.POST['fecha_nac']
            fechaFormat = datetime.datetime.strptime(fecha_nac, '%d/%m/%Y')
            profile.fecha_nac = fechaFormat
            #profile.rut = request.POST['rut']
            profile.genero = request.POST['genero']
            profile.nacionalidad = request.POST['nacionalidad']
            profile.direccion = request.POST['direccion']
            profile.region = request.POST['region']
            profile.comuna = request.POST['comuna']
            profile.estado_civil = request.POST['estado_civil']
            profile.telefono_casa = request.POST['telefono_casa']
            profile.telefono_cel = request.POST['telefono_cel']
            profile.profesion = request.POST['profesion']
            profile.universidad = request.POST['universidad']
            profile.year_titulo = request.POST['year_titulo']
            profile.empresa = request.POST['empresa']
            profile.telefono_empresa = request.POST['telefono_empresa']
            profile.direccion_empresa = request.POST['direccion_empresa']
            profile.provincia = request.POST['provincia']
            profile.save()


            message = "Sus datos han sido actualizados correctamente"

            return render(request, 'administrations/homepage.html', {'message': message})



def descargaTodo(request):

    if request.method == 'GET':

        inputpdf = PdfFileReader(open("D:/files/pdf.pdf", "rb"))

        for i in range (inputpdf.numPages):
            output = PdfFileWriter()
            output.addPage(inputpdf.getPage(i))
            with open("D:/files/document-page%s.pdf" %i, "wb") as outputStream:
                output.write(outputStream)

































