from django.contrib import admin
from django.contrib.auth.admin import User
from . models import *

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'pix', 'email', 'phone']
admin.site.register(Profile, ProfileAdmin)
