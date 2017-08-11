from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView


from apps.usuario.forms import UsuarioForm
from apps.usuario.models import Usuario



class UsuarioList(ListView):
    model = Usuario
    template_name = 'usuario/usuario_list.html'


class UsuarioCreate(CreateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'usuario/usuario_form.html'
    success_url = reverse_lazy('usuario:usuario_listar')


class UsuarioUpdate(UpdateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'usuario/usuario_form.html'
    success_url = reverse_lazy('usuario:usuario_listar')

class UsuarioDelete(DeleteView):
    model = Usuario
    template_name = 'usuario/usuario_delete.html'
    success_url = reverse_lazy('usuario:usuario_listar')


