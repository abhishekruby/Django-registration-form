import json

from django.shortcuts import render,get_object_or_404,HttpResponseRedirect
from django.http import HttpResponse

from registration_completed.models import Form
from registration_completed.forms import RegistrationForm

# Home page 
def index(request):

    context = {
        "title" : "School Page",
    }
    return render(request, 'web/index.html',context=context)


# Admin page rendering 
def userPage(request):
    students = Form.objects.all()
    context={
        "students": students
    } 
    return render(request, "user_page/index.html",context=context)




