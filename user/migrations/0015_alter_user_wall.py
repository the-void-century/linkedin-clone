# Generated by Django 4.2.2 on 2023-06-22 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0014_alter_user_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='wall',
            field=models.ImageField(blank=True, null=True, upload_to='user/wall'),
        ),
    ]
