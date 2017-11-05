# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    DeleteView,
    UpdateView,
    CreateView
)
from app.usuarios.models import usuario
# Create your views here.
class usuariosCreateView(CreateView):
    model = usuario
    field =[
        'nombre',
        'contrasena',
        'nickname'
    ]
    template_name = 'usuarios/usuario_form.html'
    succes_url = reverse_lazy('usuarios:usuario_lista')

class usuariosListView(ListView):
    model = usuario
    template_name = 'usuarios/usuario_list.html'
    context_object_name = 'usuarios'

class usuariosUpdateView(UpdateView):
    model = usuario
    field =[
        'nombre',
        'contrasena',
        'nickname'
    ]
    template_name = 'usuarios/usuario_form.html'
    succes_url = reverse_lazy('usuarios:usuario_lista')
