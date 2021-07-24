from django.shortcuts import render
import random
from django.http import JsonResponse

from blog.models import *
from django.forms.models import model_to_dict
from django.core.mail import send_mail
import requests
import json
import pandas as pd
import os


def test(request):
    return JsonResponse({"data": 11111})


def login(request):
    username_real = "Altria Vin"
    password_real = "123456"
    flag = 0;
    if request.method == "GET":
        username = request.GET.get("username")
        password = request.GET.get("password")
        if username == username_real and password == password_real:
            flag = 1;
        # print(username, password)
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username == username_real and password == password_real:
            flag = 1;
        # print(username, password)
    if flag == 1:
        print("login success")
    else:
        print("login fail")
    return render(request, "login.html")