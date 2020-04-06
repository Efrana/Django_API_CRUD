from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .form import UserRegisterForm


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success((request, f'Account Created for{username}!'))
            return redirect('blog-home')
    else:
        form = UserRegisterForm()
    return render(request, 'blog/Home.html', {'form': form})


@login_required
def welcome(request):
    return render(request, "blog/welcome.html")


def login(request):
    return render(request, "blog/login.html")


@login_required(login_url='users/profile/')
def profile(request):
    return render(request, 'blog/profile.html')
