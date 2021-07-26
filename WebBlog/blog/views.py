from django.shortcuts import render, redirect
import ast
import random
import time
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
    path = "static/blog-text/"
    files = os.listdir(path)
    contents = []
    for file in files:
        file = "static/blog-text/" + file
        with open(file, "r", encoding="utf-8") as f:
            contents.append(f.read())
    context = {"files": files, "contents": contents, "times": "2021-7-26 21:01", "length": str(500 + len(files) * 200) + "px"}
    return render(request, "blog.html", context)


def blogEditor(request):
    data = request.body.decode("utf-8")
    blogcontent = request.POST.get("blogcontent")
    flag = request.POST.get("flag")
    if flag == "1":
        # name = "static/blog-text/" + str(int(time.time())) + ".txt"
        # with open(name, "w+", encoding="utf-8") as file:
        #     file.write(blogcontent)
        return JsonResponse({"flag": "1"})
    return render(request, "blogEditor.html")


def blogSubmited(request):
    return render(request, "index.html")


def verification(request):
    return render(request, "verification.html")