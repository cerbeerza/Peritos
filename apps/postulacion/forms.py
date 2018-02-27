from django import forms
from apps.postulacion.models import Postulacion


class PostulacionForm(forms.ModelForm):
    class Meta:
        model = Postulacion

        fields = [

            'region_examen',

        ]

        labels = {

            'region_examen':'Región donde rendirá el Examén',
        }

        widgets = {

            'region_examen' : forms.Select(attrs={'class':'form-control'}),
        }