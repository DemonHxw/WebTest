from django.shortcuts import render, redirect
import ast
import random
from django.http import JsonResponse
from django.views import View
from blog.models import *
from django.forms.models import model_to_dict
from django.core.mail import send_mail
import requests
import json
import pandas as pd
import os


def login(request):
    username_real = "Altria Vin"
    password_real = "123456"
    if request.method == "GET":
        username = request.GET.get("username")
        password = request.GET.get("password")
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
    if username == username_real and password == password_real:
        return redirect("Altria Vin")
    return render(request, "login.html")


def blog(request):
    return render(request, "blog.html")


def blogEditor(request):
    data = request.body.decode("utf-8")
    blogcontent = request.POST.get("blogcontent")
    flag = request.POST.get("flag")
    # is_submit = request.POST.get("submit", "0")
    if flag == "1":
        print("blogcontent = " + str(blogcontent))
        return JsonResponse({"flag": "1"})
    # else:
    return render(request, "blogEditor.html")


def blogSubmited(request):
    return render(request, "index.html")