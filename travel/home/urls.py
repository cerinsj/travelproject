from django.urls import path
from  . import views


urlpatterns = [
    path('login/',views.samp,name="loginpage"),
    path('register/',views.test,name="registerpage"),
    path('test/',views.index),
    path('',views.index,name="homepage"),
    path('login/loginsub',views.loginurl),
    ]