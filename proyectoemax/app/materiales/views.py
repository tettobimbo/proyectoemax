# -*- coding: utf-8 -*-
#from __future__ import unicode_literals
#from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from app.materiales.models import material

#from Templates import herramientas


def crearmaterial(request):
    materiales = material.objects.order_by('id')
    template = loader.get_template('Index/index.html')
    context = {'material' : materiales}
    return HttpResponse(template.render(context, request))

def listarmaterial(request):
    materiales = material.objects.order_by('id')
    template = loader.get_template('materiales/material_lista.html')
    context = {'material' : materiales}
    return HttpResponse(template.render(context, request))

#def modificarherramienta(request):
#    herramientas = herramienta.objects.order_by('id')
#    template = loader.get_template('materiales/materiales_update.html')
#    context = {'herramienta' : herramientas}
#    return HttpResponse(template.render(context, request))

#def eliminarherramienta(request):
#    herramientas = herramienta.objects.order_by('id')
#    template = loader.get_template('materiales/materiales_eliminar.html')
#    context = {'herramienta' : herramientas}
#    return HttpResponse(template.render(context, request))
