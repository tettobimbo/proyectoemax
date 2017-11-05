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
from app.solicitudproyectos.models import solicitudproyecto
# Create your views here.
class solicitudproyectosCreateView(CreateView):
    model = solicitudproyecto
    field =[
        'fechaentrega',
        'direccion',
        'descripcion',
        'solicitante'
    ]
    template_name = 'solicitudproyectos/solicitudproyecto_form.html'
    succes_url = reverse_lazy('solicitudproyectos:solicitudproyecto_lista')

class solicitudproyectosListView(ListView):
    model = solicitudproyecto
    template_name = 'solicitudproyectos/solicitudproyecto_list.html'
    context_object_name = 'solicitudproyectos'

class solicitudproyectosUpdateView(UpdateView):
    model = solicitudproyecto
    field =[
        'fechaentrega',
        'direccion',
        'descripcion',
        'solicitante'
    ]
    template_name = 'solicitudproyectos/solicitudproyecto_form.html'
    succes_url = reverse_lazy('solicitudproyectos:solicitudproyecto_lista')
