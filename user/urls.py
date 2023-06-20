from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('',views.login_user,name='login'),
    path('registration',views.register,name='register'),
    path('homepage',views.homepage,name='homepage'),
    path('logout',views.logout_user, name='logout'),
]