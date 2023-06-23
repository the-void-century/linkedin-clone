from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect,HttpResponseForbidden,HttpResponseBadRequest
from django.urls import reverse
from django.template import loader
from . models import User,Job,Education,Skills,ChatRoom,Message,JobPost
from .forms import LoginForm, UserRegistrationForm, UserEditForm, JobPostForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
import json
from django.contrib import messages
from friendship.models import Friend, Follow, Block

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
            return HttpResponseRedirect(reverse("login"))
        else:
            return render(request, "user/registration.html",{"user_form":user_form,"error":"There was an error"})
    return render(request, "user/registration.html",{"user_form":user_form})

@login_required(login_url=login_user)
@csrf_protect
def homepage(request):
    user=request.user
    if request.method == "POST":
        user_form=UserEditForm(request.POST,instance=object)
        #print(user_form)
        if user_form.is_valid():
            user_form.save()
        else:
            print(user_form.errors)
            messages.error(request, 'Error updating your profile')
    current_user=User.objects.get(user_id=request.user.user_id)
    x=current_user.__dict__
    # print(x)
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
    # print(x)
    return render(request,"user/homepage.html",x)

@login_required(login_url=login_user)
@csrf_protect
def logout_user(request):
    logout(request)
    return redirect('login')

@login_required(login_url=login_user)
@csrf_protect
def people(request):
    user_list=list(User.objects.all())
    if request.method == 'POST':
        pass
    all_users=[]
    for user in user_list:
        if user.__dict__['username']!='admin':
            all_users.append(user)
    return render(request,"user/list_users.html",{"user_list":all_users})

@login_required(login_url=login_user)
@csrf_protect
def jobs(request):
    return HttpResponse("List of job postings(Hopefully)")

@login_required(login_url=login_user)
@csrf_protect
def update_profile(request):
    user_form=UserEditForm()
    return render(request,"user/update_profile.html",{"user_form":user_form,"first_name":request.user.first_name})

@login_required(login_url=login_user)
@csrf_protect
def chat_room(request, chat_room_id):
    chat_room = ChatRoom.objects.get(id=chat_room_id)
    messages = Message.objects.filter(chat_room_id=chat_room_id).order_by('timestamp')
    context = {'chat_room_id': chat_room_id, 'messages': messages}
    return render(request, 'user/cha••••••t_room.html', context)

@login_required(login_url=login_user)
@csrf_protect
def send_message(request, chat_room_id):
    if request.method == 'POST':
        content = request.POST.get('message', '').strip()
        if not content:
            return HttpResponseBadRequest("Message content cannot be empty.")
        chat_room = get_object_or_404(ChatRoom, id=chat_room_id)
        user = request.user
        message = Message.objects.create(chat_room=chat_room, user=user, content=content)
        return redirect('chat_room', chat_room_id=chat_room_id)
    return HttpResponseBadRequest("Invalid request method.")

@login_required(login_url=login_user)
@csrf_protect
def random_view(request,new_user_id):
    if request.method == "POST":
        pass
    current_user=User.objects.get(user_id=new_user_id)
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
    print(x)
    return render(request,"user/different_user.html",x)\

@login_required(login_url=login_user)
@csrf_protect
def create_job_post(request):
    job_form= JobPostForm()
    if request.method == 'POST':
        job_form = JobPostForm(request.POST)
        print("YEs,but not valid")
        if job_form.is_valid():
            print("Yes")
            new_job = job_form.save(commit=False)
            new_job.posted_by=request.user
            new_job.save()
            return render(request, "user/list_jobs.html",{"new_job":new_job,"message":"Job created successfully"})
        else:
            return render(request, "user/homepage.html",{"message":"There was some problem creating the job"})
    return render(request, "user/job_create.html",{"job_form":job_form})

def list_jobs(request):
    all_jobs=list(JobPost.objects.all())
    return render(request,"user/list_jobs.html",{"job_list":all_jobs})