from django.urls import path
from . import views
from Blog.views import posts, recent, create, post_delete, post_update

urlpatterns = [
    path('', views.home),
    path('test', views.test),

]
