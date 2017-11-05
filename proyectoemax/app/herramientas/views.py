# -*- coding: utf-8 -*-
#from __future__ import unicode_literals
#from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render , get_object_or_404
from app.herramientas.models import herramienta
#from Templates import herramientas


def crearherramienta(request):
    herramientas = herramienta.objects.order_by('id')
    template = loader.get_template('herramientas/herramienta_nueva.html')
    titulo = 'Heeeeramienta nueva'
    context = {'herramienta' : herramientas,
                'titulo' : titulo  }
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
