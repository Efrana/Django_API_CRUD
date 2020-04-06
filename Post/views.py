from django.shortcuts import render
from django.http import HttpResponse
from django.core.signals import request_finished
from django.dispatch import receiver, Signal
from .models import Blog


# Create your views here.
request_counter_signal = Signal(providing_args=['timestamp'])

def home(request):
    request_counter_signal.send(sender= Blog, timestamp='2020=04-01')
    return HttpResponse("Here's the signal")

def test(request):
    return HttpResponse("Here's the test signal")

@receiver(request_finished)
def post_request_receiver(sender, **kwargs):
    print("Request finished!")


@receiver(request_counter_signal)
def post_counter_signal_receiver(sender, **kwargs):
    print(kwargs)


