# Generated by Django 4.2.2 on 2023-06-21 06:59

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='project_id',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, null=True, size=None),
        ),
    ]