from django.contrib import admin
from .models import UserProfile,User,UserLibrary,Notification
from .models import Chat

admin.site.register(Chat)
admin.site.register(UserProfile)
admin.site.register(UserLibrary)
admin.site.register(Notification)

