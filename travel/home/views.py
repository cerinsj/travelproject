from django.shortcuts import render
from django.http import HttpResponse
from .models import product



p1=product()
p1.name='waffles'
p1.price=250
p1.dsc='crunchy chocolaty'

p2=product()
p2.name='pancakes'
p2.price=200
p2.dsc='delicious'

p3=product()
p3.name='smoothies'
p3.price=100
p3.dsc='healthy'

p4=product()
p4.name='choclate'
p4.price=300
p4.dsc='good'


pro=[p1,p2,p3,p4]


def index(request):
    return render(request,'test.html',{'p':pro})

def index(request):
    return render(request,'index.html')

def samp(request):    
    return render(request,'login.html')

def test(request):
    return render(request,'register.html')

def loginurl(request):
    return render(request,'test.html')
    




