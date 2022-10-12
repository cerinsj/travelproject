from django.urls import path
from  . import views
from .feed import latest_feed


urlpatterns = [
    path('',views.index,name="homepage"),
    path('test/',views.samp),
    path('login/',views.login,name="loginpage"),
    path('register/',views.register,name="registerpage"),
    path('logout/',views.logout),
    path('feed/',latest_feed())
    ]