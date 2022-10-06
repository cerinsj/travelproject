from django.urls import path
from  . import views

urlpatterns=[
    path('',views.details,name="detail_page"),
    path('cmt/',views.commenting,name="commentbox"),
    path('search2/',views.search,name='searchbox')
    ]