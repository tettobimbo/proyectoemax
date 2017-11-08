# -*- coding: utf-8 -*-
#from __future__ import unicode_literals
#from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render , get_object_or_404
from app.herramientas.models import herramienta
from app.herramientas.forms import herramientasform
#from Templates import herramientas


def crearherramienta(request):
    if request.method == 'POST':
        form = herramientasform(request.POST)
        if form.is_valid():
            herramienta = form.save()
            herramienta.save()
            return HttpResponseRedirect('/')
        else:
            form = herramientasform()
    template = loader.get_template('herramientas/herramienta_nueva.html')
    context = { 'form' : form }
    return HttpResponse(template.render(context, request))

def listarherramienta(request):
    herramientas = herramienta.objects.order_by('id')
    template = loader.get_template('herramientas/herramienta_list.html')
    context = {'herramienta' : herramientas}
    return HttpResponse(template.render(context, request))

def detaherramienta(request,pk):
    herramientas = get_object_or_404(herramienta, pk=pk)
    template =  loader.get_template('herramientas/herramienta_detalle.html')
    context = {'herramienta' : herramientas}
    return HttpResponse(template.render(context, request))

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
