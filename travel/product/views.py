from django.shortcuts import render,redirect
from .models import TravelPlace, comment
from django.http import JsonResponse
from django.core.cache import cache

def details(request):
    id=request.GET['id']
    if cache.get(id):
        pro=cache.get(id)
        print("data from cache")
    else:
        pro=TravelPlace.objects.get(id=id)
        cache.set(id,pro)
        print("data from database") 
    cmt=comment.objects.filter(place_id=id)
    res=render(request,'single.html',{'p':pro,'cmt':cmt})
    res.set_cookie('pro_name',pro.name)
    return res

def commenting(request):
    msg=request.GET['msg']
    pro_id=request.GET['pro_id']   
    user=request.GET['user']
    cmt=comment.objects.create(cmt=msg,name=user,place_id=pro_id)
    cmt.save();
    return redirect('/')

def search(request):
    sr=request.POST['searchbox']
    obj=TravelPlace.objects.filter(name__istartswith=sr)
    print(obj)
    return render(request,'index.html',{'s':sr})  

    