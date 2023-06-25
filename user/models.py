from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import AbstractUser

def user_directory_path(instance, filename):
    return "user_{0}/{1}".format(instance.user.id, filename)

class Company(models.Model):
     company_id=models.AutoField(primary_key=True)
     logo=models.ImageField(blank=True, null=True)

class Job(models.Model):
    job_id=models.AutoField(primary_key=True)
    job_title=models.CharField(max_length=100)
    company_name=models.CharField(max_length=100)
    company_id=models.IntegerField()

class Education(models.Model):
    education_id=models.AutoField(primary_key=True)
    education_title=models.CharField(max_length=100)
    insitution_name=models.CharField(max_length=100)
    score=models.IntegerField()

class Comment(models.Model):
    comment_id=models.AutoField(primary_key=True)
    comment_text=models.TextField()
    post_id=models.IntegerField()

class Posts(models.Model):
    post_id=models.AutoField(primary_key=True)
    post_name=models.CharField(max_length=100)
    post_type=models.CharField(max_length=20)
    images=ArrayField(models.ImageField(),blank=True,null=True)
    comment_id=ArrayField(models.IntegerField(),blank=True,null=True)
    

class Skills(models.Model):
    skill_id=models.AutoField(primary_key=True)
    skill_name=models.CharField(max_length=30)

class User(AbstractUser):
    user_id=models.AutoField(primary_key=True)
    username = models.CharField(max_length=100,unique=True)
    first_name = models.CharField(max_length=100,blank=True,null=True)
    last_name = models.CharField(max_length=100,blank=True,null=True)
    email = models.EmailField(max_length=100,unique=True)
    password = models.CharField(max_length=200)
    date_of_birth = models.DateField(blank=True,null=True)
    profile_picture = models.ImageField(blank=True,null=True,upload_to="user/profile_picture")
    wall = models.ImageField(blank=True,null=True,upload_to="user/wall")
    headline = models.CharField(max_length=100,blank=True,null=True)
    summary = models.TextField(max_length=1000,blank=True,null=True)
    location = models.CharField(max_length=100)
    education_id=ArrayField(models.IntegerField(),blank=True,null=True)
    job_id=ArrayField(models.IntegerField(),default=list)
    skill_id = ArrayField(models.IntegerField(),default=list)
    project_id=ArrayField(models.IntegerField(),default=list)
    friendships = models.ManyToManyField('self', through='Connection', symmetrical=False)

    def get_profile_url(self):
            try:
                 return self.profile_picture.url
            except IOError:
                 return None

    def get_wall_url(self):
            try:
                 return self.wall.url
            except IOError:
                 return None

class Project(models.Model):
    project_id=models.AutoField(primary_key=True)
    project_title=models.CharField(max_length=100)
    project_domain=models.CharField(max_length=100)

class Connection(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_connections')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_connections')
    created_at = models.DateTimeField(auto_now_add=True)


class ChatRoom(models.Model):
    name = models.CharField(max_length=100)


class Message(models.Model):
    chat_room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name='messages')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}: {self.content}"
    
class JobPost(models.Model):
    job_id=models.AutoField(primary_key=True)
    job_title=models.CharField(max_length=100)
    posted_by=models.ForeignKey(User, on_delete=models.CASCADE,default=None)
    company_title=models.CharField(max_length=100,default="Not Disclosed")
    job_summary=models.TextField()
    apply_link = models.URLField(max_length=200)
    location=models.CharField(max_length=100)