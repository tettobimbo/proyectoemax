# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render , get_object_or_404
from app.herramientas.models import herramienta
from app.herramientas.forms import herramientasform
from django.views.generic import (
    ListView,
    DetailView
)
from django.views.generic.edit import(
    DeleteView,
    UpdateView,
    CreateView
)
#from Templates import herramientas


class HerramientaCreate(CreateView):
    model = herramienta
    fields = '__all__'
    success_url = reverse_lazy('herramientas:HerramientaList')

class HerramientaUpdate(UpdateView):
    model = herramienta
    fields = '__all__'
    success_url = reverse_lazy('herramientas:HerramientaList')

class HerramientaDelete(DeleteView):
    model = herramienta
    success_url = reverse_lazy('herramientas:HerramientaList')

class HerramientaList(ListView):
    model = herramienta

class HerramientaDetail(DetailView):
    model = herramienta




















def modificarherramienta(request):
    herramientas = herramienta.objects.order_by('id')
    template = loader.get_template('herramientas/herramienta_update.html')
    context = {'herramienta' : herramientas}
    return HttpResponse(template.render(context, request))

def eliminarherramienta(request):
    herramientas = herramienta.objects.order_by('id')
    template = loader.get_template('herramientas/herramienta_eliminar.html')
    context = {'herramienta' : herramientas}
    return HttpResponse(template.render(context, request))
