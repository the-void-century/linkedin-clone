# Generated by Django 4.2.2 on 2023-06-20 13:38

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_remove_posts_comment_id_remove_posts_images_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='comment_id',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, null=True, size=None),
        ),
        migrations.AddField(
            model_name='posts',
            name='images',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.ImageField(upload_to=''), blank=True, null=True, size=None),
        ),
        migrations.AddField(
            model_name='user',
            name='education_id',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, null=True, size=None),
        ),
        migrations.AddField(
            model_name='user',
            name='job_id',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, null=True, size=None),
        ),
        migrations.AddField(
            model_name='user',
            name='skill_id',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, null=True, size=None),
        ),
    ]
