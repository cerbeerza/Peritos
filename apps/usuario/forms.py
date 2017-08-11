from django import forms

from apps.usuario.models import Usuario


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        
        fields = [
            'rut',
            'nombres',
            'apellido_p',
            'apellido_m',
            'fecha_nac',
            'email',
            'password',
            'genero',
            'nacionalidad',
            'direccion',
            'region',
            'comuna',
            'estado_civil',
            'telefono_casa',
            'telefono_cel',
            'profesion',
            'universidad',
            'year_titulo',
            'empresa',
            'telefono_empresa',
            'direccion_empresa',
            
            ]
            
        labels = { 
            'rut' : 'Rut',
            'nombres' : 'Nombres',
            'apellido_p' : 'Apellido Paterno',
            'apellido_m' : 'Apellido Materno',
            'fecha_nac' : 'Fecha Nacimiento',
            'email' : 'Email',
            'password' : 'Password',
            'genero' : 'Género',
            'nacionalidad' : 'Nacionalidad',
            'direccion' : 'Dirección',
            'region' : 'Región',
            'comuna' : 'Comuna',
            'estado_civil' : 'Estado Civil',
            'telefono_casa' : 'Teléfono Casa',
            'telefono_cel' : 'Celular',
            'profesion' : 'Profesión',
            'universidad' : 'Universidad',
            'year_titulo' : 'Año Titulación',
            'empresa' : 'Empresa',
            'telefono_empresa' : 'Teléfono Empresa',
            'direccion_empresa' : 'Dirección Empresa',
        }
        
        widgets = {
            
            'rut' : forms.TextInput(attrs={'class':'form-control'}),
            'nombres' : forms.TextInput(attrs={'class':'form-control'}), 
            'apellido_p' : forms.TextInput(attrs={'class':'form-control'}),
            'apellido_m' : forms.TextInput(attrs={'class':'form-control'}),
            'fecha_nac' : forms.DateInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
            'password' : forms.PasswordInput(attrs={'class':'form-control'}),
            'genero' : forms.Select(attrs={'class':'form-control'}),
            'nacionalidad' : forms.TextInput(attrs={'class':'form-control'}),
            'direccion' : forms.TextInput(attrs={'class':'form-control'}),
            'region' : forms.TextInput(attrs={'class':'form-control'}),
            'comuna' : forms.TextInput(attrs={'class':'form-control'}),
            'estado_civil' : forms.Select(attrs={'class':'form-control'}),
            'telefono_casa' : forms.NumberInput(attrs={'class':'form-control'}),
            'telefono_cel' : forms.NumberInput(attrs={'class':'form-control'}),
            'profesion' : forms.TextInput(attrs={'class':'form-control'}),
            'universidad' : forms.TextInput(attrs={'class':'form-control'}),
            'year_titulo' : forms.NumberInput(attrs={'class':'form-control'}),
            'empresa' : forms.TextInput(attrs={'class':'form-control'}),
            'telefono_empresa' : forms.NumberInput(attrs={'class':'form-control'}),
            'direccion_empresa' : forms.TextInput(attrs={'class':'form-control'}),
            
        }