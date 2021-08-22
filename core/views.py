from django.http import HttpResponse
from django.template import  Context, Template
from django.shortcuts import render

def hello (request):
    t = Template('hello, {{ name }} !')
    c = Context({'name': 'Maxim'})
    return HttpResponse (t.render(c))
