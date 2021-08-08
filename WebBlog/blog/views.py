from django.shortcuts import render, redirect
import ast
import random
import time
from django.http import JsonResponse
from django.views import View
from mdx_math import MathExtension

from blog.models import *
from django.forms.models import model_to_dict
from django.core.mail import send_mail
import requests
import json
import pandas as pd
import os
import markdown

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
    class blogTest:
        def __init__(self, title, content, time):
            self.title = title
            self.content = content
            self.time = time
    Blog = []
    path = "static/blog-text/"
    files = os.listdir(path)
    contents = []
    for file in files:
        file = "static/blog-text/" + file
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()
            BlogTmp = blogTest(title=file[17:-3], content=content, time="2021-7-26 21:01")
            Blog.append(BlogTmp)
    length = str(500 + len(files) * 200) + "px"
    return render(request, "blog.html", context={"Blog": Blog, "length": length})


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


def blogShow(request):
    # exts = ['markdown.extensions.extra', 'markdown.extensions.codehilite', 'markdown.extensions.tables',
    #         'markdown.extensions.toc', MathExtension(enable_dollar_delimiter=True)]
    exts = ['markdown.extensions.extra', 'markdown.extensions.codehilite', 'markdown.extensions.tables',
            'markdown.extensions.toc']
    filename = request.GET.get("blogname")
    fileName = "static/blog-text/" + filename + ".md"
    # print(fileName)
    with open(fileName, "r+", encoding="utf-8") as file:
        content = file.read()
    ret = markdown.markdown(content, extensions=exts)
    # print(ret, type(ret))
    with open("templates/blogTmp.html", "w+", encoding="utf-8") as file:
        # print(file.read())
        file.write(ret)
    return render(request, "blogShow.html")


def blogSubmited(request):
    return render(request, "index.html")


def verification(request):
    return render(request, "verification.html")