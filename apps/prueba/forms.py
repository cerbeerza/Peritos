from django import forms
from apps.prueba.models import Prueba

class PruebaForm(forms.ModelForm):
    class Meta:
        model = Prueba

        fields = [

            'rut',
            'nombre',
            'region',
            'parte_a',
            'parte_b',
            'parte_final',
            'nota',
            'situacion',
            'periodo',
            'rutx',

        ]

        labels = {

            'rut':'Rut',
            'nombre':'Nombre',
            'region': 'Región Exámen',
            'parte_a':'Parte A',
            'parte_b':'Parte B',
            'parte_final':'Puntaje Total',
            'nota':'Nota',
            'situacion':'Situación',
            'periodo':'Periodo',
            'rutx':'RutX',

        }


        