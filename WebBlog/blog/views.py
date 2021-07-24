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
    if request.method == "GET":
        username = request.GET.get("username")
        password = request.GET.get("password")
        print(username, password)
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username, password)
    return render(request, "login.html")