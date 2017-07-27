# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import Username
from django.contrib import messages

def index(request):
    return render(request, 'user_validation/index.html')

def create(request):
    if len(Username.objects.filter(username=request.POST['name'])) > 0:
        messages.error(request, 'That username is already registered!')
        return redirect("/")
    else:
        if 7 < len(request.POST['name']) < 27:
            Username.objects.create(username=request.POST['name'])
            messages.success(request, 'The username you entered (' + request.POST['name'] + ') is valid. Thank you!')
            return redirect("/success")
        else:
            messages.error(request, 'Username needs to be between 8 and 26 characters long, buddy.')
            return redirect("/")
def success(request):
    context = {
    "usernames": Username.objects.all()}
    return render(request, 'user_validation/success.html', context)

def delete(request, id):
    context = {
        "username" : Username.objects.get(id=id),
    }
    Username.objects.filter(id=id).delete()
    messages.success(request, 'Removed the offending name!')
    return redirect("/success")
