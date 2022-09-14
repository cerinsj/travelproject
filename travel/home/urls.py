from django.urls import path
from  . import views


urlpatterns = [
    path('login/',views.samp),
    path('register/',views.test),
    path('test/',views.index),
    path('',views.index),
    path('login/loginsub',views.loginurl)
]