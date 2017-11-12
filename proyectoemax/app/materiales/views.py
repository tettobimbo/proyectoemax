# -*- coding: utf-8 -*-
#from __future__ import unicode_literals
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from app.materiales.models import material
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
    )
#from Templates import herramientas

class MaterialesList(ListView):
    model = material

class MaterialesDetail(DetailView):
    model = material

class MaterialesCreate(CreateView):
    model = material
    fields = '__all__'
    success_url = reverse_lazy('materiales:MaterialesList')

class MaterialesUpdate(UpdateView):
    model = material
    fields = '__all__'
    success_url = reverse_lazy('materiales:MaterialesList')

class MaterialesDelete(DeleteView):
    model = material
    success_url = reverse_lazy('materiales:MaterialesList')
