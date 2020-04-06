from django.urls import path
from . import views
from Blog.views import posts, recent, create, post_delete,post_update

urlpatterns = [
    path('', views.home),

    path('posts/', posts),
    path('recent-posts/', recent),
    path('create/', create),
    path('delete/<int:id>/', post_delete),
    path('update/', post_update),

]
