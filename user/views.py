from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from . models import User
from .forms import LoginForm, UserRegistrationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def login_user(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("homepage"))
    if request.method == "POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            user=authenticate(request,username=cd['username'],password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return render(request,"user/homepage.html",{})
                else:
                    return HttpResponse("The user is not active")
            else:
                return HttpResponse("Invalid username or password")
    user_form=LoginForm()
    return render(request, "user/index.html",{"user_form": user_form})

@csrf_protect
def register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("homepage"))
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        print(user_form)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, "user/register_done.html",{"new_user":new_user})
    user_form=UserRegistrationForm()
    return render(request, "user/registration.html",{"user_form":user_form})

@login_required(login_url=login_user)
def homepage(request):
    if request.method == "POST":#creating a new post
        pass
    current_user = request.user
    print(current_user.user_id)
    return render(request,"user/homepage.html",{})

@login_required(login_url=login_user)
def logout_user(request):
    logout(request)
    return redirect('login')