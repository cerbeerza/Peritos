from django import forms

from apps.mensura.models import MensuraGeneral


class MensuraGeneralForm(forms.ModelForm):
    class Meta:
        model = MensuraGeneral
        
        fields = [
            'periodo',
            'num_mensura',
            'promedio',
            'empresa',
            'situacion',
            'usuario',
            
            
            ]
            
        labels = { 
            'periodo' : 'Periodo',
            'num_mensura' : 'Cantidad Mensuras',
            'promedio' : 'Promedio',
            'empresa' : 'Empresa',
            'situacion' : 'Situación',
            'usuario' : 'Usuario',
            
        }
        
        widgets = {
            
            'periodo' : forms.TextInput(attrs={'class':'form-control'}),
            'num_mensura' : forms.TextInput(attrs={'class':'form-control'}),
            'promedio' : forms.TextInput(attrs={'class':'form-control'}),
            'empresa' : forms.TextInput(attrs={'class':'form-control'}),
            'situacion' : forms.TextInput(attrs={'class':'form-control'}),
            'usuario' : forms.TextInput(attrs={'class':'form-control'}),
            
        }