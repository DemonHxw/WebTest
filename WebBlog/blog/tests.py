from django.test import TestCase
import ast
# Create your tests here.
import os

name = "static/blog-text/"
files = os.listdir(name)
print(files)