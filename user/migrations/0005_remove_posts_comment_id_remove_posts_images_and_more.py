# Generated by Django 4.2.2 on 2023-06-20 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_user_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='comment_id',
        ),
        migrations.RemoveField(
            model_name='posts',
            name='images',
        ),
        migrations.RemoveField(
            model_name='user',
            name='education_id',
        ),
        migrations.RemoveField(
            model_name='user',
            name='job_id',
        ),
        migrations.RemoveField(
            model_name='user',
            name='skill_id',
        ),
    ]
