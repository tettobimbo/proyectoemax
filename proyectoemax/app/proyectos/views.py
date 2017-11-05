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
from app.proyectos.models import proyecto

class proyectosCreateView(CreateView):
    model = proyecto
    field =[
        'fechaentrega',
        'direccion',
        'descripcion',
        'encargado',
        'totalherramientas',
        'totalmaterial',
        'usuario',
        'material',
        'herramienta'

    ]
    template_name = 'proyectos/proyecto_form.html'
    succes_url = reverse_lazy('proyectos:proyecto_lista')

class proyectosListView(ListView):
    model = proyecto
    template_name = 'proyectos/proyecto_list.html'
    context_object_name = 'proyectos'

class proyectosUpdateView(UpdateView):
    model = proyecto
    field =[
        'fechaentrega',
        'direccion',
        'descripcion',
        'encargado',
        'totalherramientas',
        'totalmaterial',
        'usuario',
        'material',
        'herramienta'
    ]
    template_name = 'proyectos/proyecto_form.html'
    succes_url = reverse_lazy('proyectos:proyecto_lista')
