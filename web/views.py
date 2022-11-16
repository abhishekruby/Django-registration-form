from django.shortcuts import render

# Create your views here.
def index(request):

    context = {
        "title" : "Fo Page",
    }
    return render(request, 'web/index.html',context=context)



