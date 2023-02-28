from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse('HOME')


def index(request):
    return HttpResponse("Hello world")

def aboutus(request):
    return render(request,'aboutus.html')

def contactus(request):
    name = "root"
    email = "root@gmail.com"
    return render(request,'blog/contactus.html',{'name':name,'email':email})

def feedback(request):
    username="parth"
    useremail = "parth@gmail.com"
    context ={
        'username':username,
        'useremail':useremail,
    }
    return render(request,'blog/feedback.html',context)