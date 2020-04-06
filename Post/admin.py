from django.contrib import admin

# Register your models here.
from .models import *

class BlogAdmin(admin.ModelAdmin):
    list_display = ['title','body']
admin.site.register(Blog, BlogAdmin)