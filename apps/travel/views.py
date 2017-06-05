# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import userDB, plan

def index(request):
    return render(request,"travel/index.html")

# def login(request):
#     if request.method == "POST":
#         response = userDB.objects.check_log(request.POST)
#         if not request[0]:
#             for message in response[1]:
#                 message.error(request, message[1])
#             return redirect('travel: index')
#         else:
#             request.session['user'] = {
#             "id": response[1].id,
#             "name": response[1].name,
#             "username": response[1].username,
#             }
#             return redirect('travel:landing')
#     return redirect('travel:index')

def log_register(request):
    response = [0]
    if request.method == "POST":
        if request.POST["choose"] == "register":
            response = userDB.objects.check_create(request.POST)
        elif request.POST["choose"] == "login":
            response = userDB.objects.check_log(request.POST)
        if not response[0]:
            for message in response[1]:
                messages.error(request, message[1])
            return redirect('/')
        else:
            request.session['user'] = {
            "id": response[1].id,
            "name": response[1].name,
            "username": response[1].username,
            }
            return redirect('travel:landing')
    return redirect('/')

def landing(request):
    return render(request, "travel/landing.html")

def logout(request):
    request.session.clear()
    return redirect('/')

def add(request):
    pass
    return redirect('travel: landing')

def destination(request):
    pass
    return render(request, "travel/destination.html")



# Create your views here.
