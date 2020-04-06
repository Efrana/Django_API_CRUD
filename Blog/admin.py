from django.contrib import admin

# Register your models here.
from .models import *

class PostAdmin(admin.ModelAdmin):
    list_display = ['title','body','date_posted']
    list_per_page = 5
    list_max_show_all = 10
admin.site.register(Post, PostAdmin)