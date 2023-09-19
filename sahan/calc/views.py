from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'home.html',{'name':'Sahan'}) #html page path , name is dynamic

def add(request):

    val1 = int(request.POST['num1'])#to fax data use Get
    val2 = int(request.POST['num2'])#to submit data usew Post
    res = val1 + val2
    return render(request,'result.html',{'result':res})
