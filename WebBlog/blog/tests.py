from django.test import TestCase
import ast
# Create your tests here.

content = str({"blogcontent":"fjisdaojfisod","flag":1})
contentDict = ast.literal_eval(content)

print(contentDict, type(contentDict))
print(content, type(content))
