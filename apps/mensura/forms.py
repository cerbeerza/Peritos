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
            'usuario_id',
        ]

        labels = {

            'periodo':'Periodo',
            'num_mensura':'N° de Mensuras',
            'promedio':'promedio',
            'empresa':'Empresa',
            'situacion':'Situación',
            'usuario_id':'Id de Usuario',
        }

        widgets = {

            'periodo': forms.TextInput(attrs={'class': 'form-control'})
        }


