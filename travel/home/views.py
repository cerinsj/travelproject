from logging.handlers import DatagramHandler
from django.shortcuts import render
from django.http import HttpResponse
from product.models import TravelPlace

def index(request):
    data=TravelPlace.objects.all()
    return render(request,'index.html',{'d':data})

def samp(request):    
    return render(request,'login.html')

def test(request):
    return render(request,'register.html')

def loginurl(request):
    return render(request,'test.html')
    




