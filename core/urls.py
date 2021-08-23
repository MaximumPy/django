from django.urls import path
import core.views

urlpatterns = [

    path('', core.views.hello),
    path('stud/', core.views.stud),
    path('Students/', core.views.Students, name='stud_name'),
]
