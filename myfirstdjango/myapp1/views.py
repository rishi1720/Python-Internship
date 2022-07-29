from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def homepageview(request):
    
    return render(request, 'home.html',{'name':'rishi'})


def aboutpageview(request):
    return render(request, 'about.html')


def contactpageview(request):
    return render(request, 'contact us.html')


    
def processpageview(request):
    a= request.post ['txt1']
    b= request.post ['txt2']
    c= a+b 
    return render(request,'ans.html',{'sum':c})

