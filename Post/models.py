from django.db import models
from django.db.models.signals import post_save, pre_save,post_delete,pre_delete
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    def __str__(self):
        return self.title

def save_post(sender , instance, **kwargs):
    print(" somethig")

def after_delete_post(sender , instance, **kwargs):
    print(" delete the post")

pre_save.connect(save_post,sender=Blog)
post_save.connect(save_post, sender=Blog)
post_delete.connect(after_delete_post, sender=Blog)
pre_delete.connect(after_delete_post, sender=Blog)
