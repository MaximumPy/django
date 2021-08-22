from django.http import HttpResponse
from django.template import Context, Template
from django.shortcuts import render
import core.models

def hello (request):
    students = core.models.Students.objects.all()
    c = Context({'name': 'Maxim'})
    return render(request, 'core/hello.html', {'object_list': students})
