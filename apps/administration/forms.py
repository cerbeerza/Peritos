from django import forms
from django.contrib.auth.models import User
from apps.administration.models import Profile




class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile

        fields = [

            'direccion',
            'telefono_cel',
            'apellido_p',
            'apellido_m',
            'comuna',
            'direccion_empresa',
            'empresa',
            'estado_civil',
            'fecha_nac',
            'genero',
            'nacionalidad',
            'nombres',
            'profesion',
            'region',
            'telefono_casa',
            'telefono_empresa',
            'universidad',
            'year_titulo',
            'rut',
            'provincia',



        ]

        labels = {

            'direccion' : 'Dirección',
            'telefono_cel' : 'Celular (Formato +569 XXXXXXXX)',
            'apellido_p' : 'Apellido Paterno',
            'apellido_m' : 'Apellido Materno',
            'comuna' : 'Comuna',
            'direccion_empresa' : 'Dirección Empresa',
            'empresa' : 'Empresa',
            'estado_civil' : 'Estado Civil',
            'fecha_nac' : 'Fecha de Nacimiento',
            'genero' : 'Género',
            'nacionalidad' : 'Nacionalidad',
            'nombres' : 'Nombres',
            'profesion' : 'Profesión',
            'region' : 'Región',
            'telefono_casa' : 'Teléfono Particular',
            'telefono_empresa' : 'Teléfono Empresa',
            'universidad' : 'Universidad',
            'year_titulo' : 'Año Titulación',
            'rut' : 'Rut (Formato XXXXXXXX-X)',
            'provincia':'Provincia',


        }

        widgets = {

            'direccion' : forms.TextInput(attrs={'class':'form-control'}),
            'telefono_cel' : forms.TextInput(attrs={'class':'form-control'}),
            'nombres' : forms.TextInput(attrs={'class':'form-control'}),
            'profesion' : forms.Select(attrs={'class':'form-control'}),
            'region' : forms.Select(attrs={'class':'form-control'}),
            'telefono_casa' : forms.TextInput(attrs={'class':'form-control'}),
            'telefono_empresa' : forms.TextInput(attrs={'class':'form-control'}),
            'universidad' : forms.TextInput(attrs={'class':'form-control'}),
            'year_titulo' : forms.TextInput(attrs={'class':'form-control'}),
            'apellido_p' : forms.TextInput(attrs={'class':'form-control'}),
            'apellido_m' : forms.TextInput(attrs={'class':'form-control'}),
            'comuna' : forms.Select(attrs={'class':'form-control'}),
            'direccion_empresa' : forms.TextInput(attrs={'class':'form-control'}),
            'empresa' : forms.TextInput(attrs={'class':'form-control'}),
            'estado_civil' : forms.Select(attrs={'class':'form-control'}),
            'fecha_nac' : forms.DateInput(attrs={'class':'form-control','readonly':'true'}),
            'genero' : forms.Select(attrs={'class':'form-control'}),
            'nacionalidad' : forms.TextInput(attrs={'class':'form-control'}),
            'rut' : forms.TextInput(attrs={'class':'form-control', 'onblur' : 'Rut(rut.value)'}),
            'provincia': forms.Select(attrs={'class':'form-control'}),


        }

class UserForm(forms.ModelForm):
    class Meta:
        model = User

        fields = [


                    'password',
                    'email',

                ]

        labels = {


                    'password': 'Password',
                    'email': 'Email',

                }

        widgets = {


                    'password': forms.PasswordInput(attrs={'class': 'form-control'}),
                    'email': forms.EmailInput(attrs={'class': 'form-control'}),

                }

