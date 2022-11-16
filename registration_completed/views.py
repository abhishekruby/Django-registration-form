from django.shortcuts import render

# Create your views here.
def registration_form(request):
    context={}
    return render(request,'web/form.html',context=context)