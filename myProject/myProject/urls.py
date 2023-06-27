from django.contrib import admin
from django.urls import path,include
from myApp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('',include("myApp.urls")),
]
