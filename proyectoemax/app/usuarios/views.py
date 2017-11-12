# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.views.generic import (
    ListView,
    DetailView
)
from django.views.generic.edit import(
    DeleteView,
    UpdateView,
    CreateView
)
# Create your views here.

def authentication(request):
        action = request.POST.get('action',None)
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user = authenticate(username=username, password=password )
        if user is not None:
            login(request, user)
            return render(request, 'index/index.html', {})
        else:
            return render(request, 'auth/login.html', {})

def logout_view(request):
    logout(request)
    return render(request, 'auth/login.html', {})

class UsuarioList(ListView):
    model = User

class UsuarioCreate(CreateView):
    model = User
    fields = '__all__'
    success_url = reverse_lazy('usuarios:UsuarioList')

class UsuarioUpdate(UpdateView):
    model = User
    fields = '__all__'
    success_url = reverse_lazy('usuarios:UsuarioList')

class UsuarioDelete(DeleteView):
    model = User
    success_url = reverse_lazy('usuarios:UsuarioList')

class UsuarioDetail(DetailView):
    model = User
