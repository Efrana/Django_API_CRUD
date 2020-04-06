from django.contrib import admin

# Register your models here.
# Register your models here.
from .models import *
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','image']
admin.site.register(Profile, ProfileAdmin)
