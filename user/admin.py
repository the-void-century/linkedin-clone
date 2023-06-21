from django.contrib import admin
from .models import User,Skills,Education,Job

# Register your models here.
admin.site.register(User)
admin.site.register(Skills)
admin.site.register(Education)
admin.site.register(Job)