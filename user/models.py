from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import AbstractUser

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
    profile_picture = models.ImageField(blank=True,null=True)
    headline = models.CharField(max_length=100,blank=True,null=True)
    summary = models.TextField(max_length=1000,blank=True,null=True)
    location = models.CharField(max_length=100)
    education_id=ArrayField(models.IntegerField(),blank=True,null=True)
    job_id=ArrayField(models.IntegerField(),blank=True,null=True)
    skill_id = ArrayField(models.IntegerField(),blank=True,null=True)
