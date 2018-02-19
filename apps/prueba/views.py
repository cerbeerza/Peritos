from django.shortcuts import render
from django.views.generic import ListView


from apps.prueba.models import Prueba



class PruebaList(ListView):
    model = Prueba
    template_name = 'prueba/prueba_list.html'