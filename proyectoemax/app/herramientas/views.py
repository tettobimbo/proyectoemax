# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render , get_object_or_404
from app.herramientas.models import herramienta
from app.herramientas.forms import herramientasform
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, cm
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

def reporte(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=ListadoHerramientas.pdf'
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)

    #HEADER
    c.setLineWidth(.3)
    c.setFont('Helvetica',22)
    c.drawString(30,750,'EMAX')
    c.setFont('Helvetica',12)
    c.drawString(30,735,'Listado de herramientas')

    c.setFont('Helvetica-Bold',12)
    c.drawString(480,750,'13/11/2017')

    c.line(460,747,560,747)

    #ESTILO DE TABLA
    styles=getSampleStyleSheet()
    styleBH = styles["Normal"]
    styleBH.alignment = TA_CENTER
    styleBH.fontSize = 10

    nombre = Paragraph('''Nombre''',styleBH)
    existencias = Paragraph('''Existencias''',styleBH)
    preciounitario = Paragraph('''Precio Unitario''',styleBH)

    data=[]
    data.append([Nombre, Existencias,Precio unitario])

    #ESTILO DE TABLA




    #SAVE PDF
    c.save()
    pdf=buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response
