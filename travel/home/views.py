from logging.handlers import DatagramHandler
from django.shortcuts import render,redirect
from django.http import HttpResponse
from product.models import TravelPlace
from django.contrib.auth.models import User,auth

def index(request):
    if request.method=="POST":
        val=request.POST['searchbox']
        data=TravelPlace.objects.filter(name__istartswith=val)
    else:
        data=TravelPlace.objects.all()
    return render(request,'index.html',{'d':data})

def samp(request):    
    return render(request,'login.html')

def test(request):
    if request.method=='POST':
        uname=request.POST['uname']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pword=request.POST['pword']
        confpword=request.POST['confpword']
        ucheck=User.objects.filter(username=uname)
        echeck=User.objects.filter(email=email)
        if ucheck:
            msg="Username already exist!!"
            return render(request,'register.html',{'msg':msg})
        elif echeck:
            msg="Email already exist!!"
            return render(request,'register.html',{'msg':msg})
        elif pword!=confpword:
            msg="Password doesn't match!!"
            return render(request,'register.html',{'msg':msg})
        else:
            user=User.objects.create_user(username=uname,first_name=fname,last_name=lname,email=email,password=pword)
            user.save();
            return redirect('/')
    
    return render(request,'register.html')

def loginurl(request):
    uname=request.POST['uname']
    pname=request.POST['pword']
    user=auth.authenticate(username=uname,password=pname)
    if user is not None:
        auth.login(request,user)
        return redirect('/')
    else:
        return render(request,'test.html')




    




