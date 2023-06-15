from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, 'wlabs/home.html')

def about(request):
    return render(request, 'wlabs/about.html')

def products(request):
    return render(request, 'wlabs/products.html')

def services(request):
    return render(request, 'wlabs/services.html')

def tutorials(request):
    return render(request, 'wlabs/tutorials.html')

def signin(request):
    return render(request, 'wlabs/signin.html')

def signup(request):
    return render(request, 'wlabs/signup.html')