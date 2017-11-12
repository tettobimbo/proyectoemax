# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render , get_object_or_404
from app.proyectos.models import proyecto
from app.proyectos.forms import proyectoform
from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    DeleteView,
    UpdateView,
    CreateView
)


class ProyectoCreate(CreateView):
    model = proyecto
    fields = '__all__'
    success_url = reverse_lazy('proyectos:ProyectoList')

class ProyectoUpdate(UpdateView):
    model = proyecto
    fields = '__all__'
    success_url = reverse_lazy('proyectos:ProyectoList')

class ProyectoDelete(DeleteView):
    model = proyecto
    success_url = reverse_lazy('proyectos:ProyectoList')

class ProyectoList(ListView):
    model = proyecto

class ProyectoDetail(DetailView):
    model = proyecto
