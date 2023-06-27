from django.contrib import admin
from django.urls import path, include
from . import views
from myApp.views import search_data
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name="home"),
    path('signup/',views.signuppage,name='signup'),
    path('login',views.loginpage,name='login'),
    path('logout',views.logoutUser,name='logout'),
    path('application',views.application,name='application'),
    path('feedbach',views.feedbach,name='feedbach'),
    path('search_result/', views.search_data, name='search_result'),
]