from django.contrib import admin
from .models import User,Skills,Education,Job,Project,ChatRoom

# Register your models here.
admin.site.register(User)
admin.site.register(Skills)
admin.site.register(Education)
admin.site.register(Job)
admin.site.register(Project)
admin.site.register(ChatRoom)