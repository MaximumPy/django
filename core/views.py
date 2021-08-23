from django.http import HttpResponse
from django.template import Context, Template
from django.shortcuts import render
from django.views.generic import TemplateView
import core.models

class indexViev(TemplateView):
    template_name = 'core/index.html'

def hello (request):
    students = core.models.Students.objects.all()
    return render(request, 'core/index.html', {'object_list': students})

def stud (request):
    return render(request, 'core/stud.html')

def Students (request):
    queryset = core.models.Students.objects.all()
    name = request.filter(name__istrtswith=name)
    students = core.models.Students.objects.all()
    c = Context({'name': 'Maxim'})
    return render(request, 'core/stud.html', {'object_list': queryset})