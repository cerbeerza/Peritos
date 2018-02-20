from django.shortcuts import render
from django.views.generic import ListView
from apps.prueba.models import Prueba



class PruebaList(ListView):

    model = Prueba
    queryset =  Prueba.objects.filter(periodo='2016')
    template_name = 'prueba/prueba_list.html'


def pruebaListFn(request):
    resultado = Prueba.objects.filter(periodo='2015')

    return render(request, 'templates/prueba/prueba_list.html',{'objeto': resultado} )

