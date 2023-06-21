from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from . models import User,Job,Education,Skills
from .forms import LoginForm, UserRegistrationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
import json

@csrf_protect
def login_user(request):
    user_form=LoginForm()
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
                    return render(request,"user/index.html",{"error":"Inactive user","user_form": user_form})
            else:
                return render(request,"user/index.html",{"error":"Invalid username or password","user_form": user_form})
    return render(request, "user/index.html",{"user_form": user_form})

@csrf_protect
def register(request):
    user_form=UserRegistrationForm()
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("homepage"))
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        print("YEs,but not valid")
        if user_form.is_valid():
            print("Yes")
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, "user/register_done.html",{"new_user":new_user})
        else:
            return render(request, "user/registration.html",{"user_form":user_form})
    return render(request, "user/registration.html",{"user_form":user_form})

@login_required(login_url=login_user)
def homepage(request):
    if request.method == "POST":#creating a new post
        pass
    current_user=User.objects.get(user_id=request.user.user_id)
    x=current_user.__dict__
    experiences=[]
    educations=[]
    skills=[]
    for i in x['job_id']:
        experiences.append(Job.objects.get(job_id=i).__dict__)
        educations.append(Education.objects.get(education_id=i).__dict__)
        skills.append(Skills.objects.get(skill_id=i).__dict__)
    x['educations']=educations
    x['experiences']=experiences
    x['skills']=skills
    #print(x)
    return render(request,"user/homepage.html",x)

@login_required(login_url=login_user)
def logout_user(request):
    logout(request)
    return redirect('login')