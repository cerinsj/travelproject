from logging.handlers import DatagramHandler
from django.shortcuts import render,redirect
from django.http import HttpResponse
from product.models import TravelPlace
from django.contrib.auth.models import User,auth

def index(request):
    # cookies_views
    if 'pro_name' in request.COOKIES:
        msg=request.COOKIES['pro_name']
    else:
        msg='What Say Our Clients!!'
    # searching
    if request.method=="POST":
        val=request.POST['searchbox']
        data=TravelPlace.objects.filter(name__istartswith=val)
    else:
        data=TravelPlace.objects.all()
    return render(request,'index.html',{'d':data,'msg':msg})

def samp(request):    
    return render(request,'login.html')

def register(request):
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
    else:
        return render(request,'register.html')

def login(request):
    if request.method=='POST':
        uname=request.POST['uname']
        pname=request.POST['password']
        user=auth.authenticate(username=uname,password=pname)
        if user is not None:
            auth.login(request,user)
            res=redirect('/')
            res.set_cookie('name',uname)
            return res
        else:
            return render(request,'login.html',{'msg':'invalid username and password'})
    else:
        return render(request,'login.html')



def logout(request):
    auth.logout(request)
    dec=redirect('/')
    dec.delete_cookie('name')
    return dec

    




