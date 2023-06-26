from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.login_user,name='login'),
    path('registration',views.register,name='register'),
    path('homepage',views.homepage,name='homepage'),
    path('logout',views.logout_user, name='logout'),
    path('people',views.people,name='people'),
    path('jobs',views.jobs,name='jobs'),
    path('update',views.update_profile,name='update'),
    path('chat/<int:chat_room_id>', views.chat_room,name='course_chat_room'),
    path('chat/<int:chat_room_id>/send_message', views.send_message, name='send_message'),
    path('different/<int:new_user_id>',views.random_view,name='random_view'),
    path('friendship/', include('friendship.urls')),
    path('job',views.create_job_post,name='create_job_post'),
    path('joblist',views.list_jobs,name='list_jobs'),
    path('connectWith/<int:user_id>',views.connect,name='connection'),
    path('disconnectWith/<int:user_id>',views.disconnect,name='disconnection'),
    path('connectedPeople',views.connected_list,name='connectedPeople')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)