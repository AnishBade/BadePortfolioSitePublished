from django.shortcuts import render
from django.http import HttpResponse
from home.models import Contact
def home(request):
    # return HttpResponse("This is my homepage(/)")
    context = {'name':'Anish','course':'Django'}
    return render(request,'home.html',context)

def about(request):
    # return HttpResponse("This is my about page(/about)")
    return render(request,'about.html')

def projects(request):
    # return HttpResponse("This is my projects page(/projects)")
    return render(request,'projects.html')

def contact(request):
    if(request.method=="POST"):
        name= request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        concern=request.POST['concern']
        print(name,email,phone,concern)
        ins=Contact(name=name,email=email,phone=phone,concern=concern)
        ins.save()
        print("The data has been written to the db")
    # return HttpResponse("This is my contact page(/contact)")
    return render(request,'contact.html')

# Create your views here.
