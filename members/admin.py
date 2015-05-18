from django.contrib import admin
from .models import Profile, Message


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['owner_name', 'institution', 'role', 'status']


class MessageAdmin(admin.ModelAdmin):
    list_display = ['sender_name', 'receiver_name', 'title', 'status']


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Message, MessageAdmin)