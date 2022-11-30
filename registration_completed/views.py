import json

from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse

from registration_completed.forms import RegistrationForm
from registration_completed.models import Form


# Create your views here.
def registration_form(request):

    if request.method == "POST":
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save();
            response_data = {
                    "title": "Successfully submitted",
                    "message": "Successfully submitted",
                    "status": "success",
                    "redirect": "yes",
                    "redirect_url": "/"
            }
            return HttpResponse(json.dumps(response_data), content_type='application/json')  
        else:
            context={
            "form" : form
            }
            return render(request,'web/form.html',context=context)
        
    else:
        data={
            "first_name":"Abhishek",
            "last_name":"Ruby",
            "gender":"",
            "degree":"other",
            "email":"abhishekruby94@gmail.com",
            "number":"9727851561",
            "description":"Stay positive",
        }
        form = RegistrationForm(initial=data)
        context={
            "form" : form
        }
        return render(request,'web/form.html',context=context)

# Applicant form Edit function    
def edit(request,id):
    student = get_object_or_404(Form,id=id)
    print(student)
    if request.method == "POST":
        form = RegistrationForm(request.POST, request.FILES,instance=student)
        if form.is_valid():
            form.save();
            response_data = {
                    "title": "Successfully submitted",
                    "message": "Successfully submitted",
                    "status": "success",
                    "redirect": "yes",
                    "redirect_url": "/userPage/"
            }
            return HttpResponse(json.dumps(response_data), content_type='application/json')  
    else:
        form = RegistrationForm(instance=student)
        context={
            "form" : form
        }
        return render(request,'web/form.html',context=context)


# Applicant form delete function
def delete(request,id):
    student = get_object_or_404(Form,id=id)
    student.delete()
    response_data = {
                        "title": "Successfully Deleted",
                        "message": "Application Successfully Deleted",
                        "status": "success",
                        "redirect": "yes",
                    }
    return HttpResponse(json.dumps(response_data), content_type='application/json')            