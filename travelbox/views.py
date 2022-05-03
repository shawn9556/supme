from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.


def index(request):
    
    return render(request, 'travelbox/travelbox.html')

    
def test(request):
    
    return render(request, 'travelbox/test.html')