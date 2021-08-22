from django.http import HttpResponse
from django.template import Context, Template
from django.shortcuts import render

def hello (request):
    c = Context({'name': 'Maxim'})
    return render(request, 'core/hello.html', {'name': request.GET['name']})
