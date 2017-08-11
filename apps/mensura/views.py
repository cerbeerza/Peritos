from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView


from apps.mensura.forms import MensuraGeneralForm
from apps.mensura.models import MensuraGeneral



class MensuraGeneralList(ListView):
    model = MensuraGeneral
    template_name = 'mensura/mensura_general_list.html'


class MensuraGeneralCreate(CreateView):
    model = MensuraGeneral
    form_class = MensuraGeneralForm
    template_name = 'mensura/mensura_general_form.html'
    success_url = reverse_lazy('mensura:mensura_general_listar')


class MensuraGeneralUpdate(UpdateView):
    model = MensuraGeneral
    form_class = MensuraGeneralForm
    template_name = 'mensura/mensura_general_form.html'
    success_url = reverse_lazy('mensura:mensura_general_listar')

class MensuraGeneralDelete(DeleteView):
    model = MensuraGeneral
    template_name = 'mensura/mensura_general_delete.html'
    success_url = reverse_lazy('mensura:mensura_general_listar')


    
