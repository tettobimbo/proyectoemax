# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

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
            return render(request, 'usuarios/login.html', {})

#def logout_view(request):
#    logout(request)
#    return render(request, 'usuarios/login.html', {})
    # Redirect to a success page.
