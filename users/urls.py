from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register),
    path('welcome/', views.welcome),
    path('profile/', views.profile),
    # path('/activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.activate),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html')),


]
