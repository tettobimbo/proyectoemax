# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.

def authentication(request):
    if request.method == 'POST':
        action = request.POST.get('action',None)
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        if action == 'signup':
            user = User.objects.create_user(username=username,password=password)
            user.save()
        elif action == 'login':
            user = authenticate(username=username, password=password )
            login(request, user)
    return render(request, 'usuarios/login.html', {})
