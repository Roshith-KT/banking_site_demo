from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User


# Create your views here.

def index(request):
    return render(request, 'index.html')

def buttonpage(request):
    return render(request,'buttonpage.html')

def details(request):
    return render(request,'form.html')

def message(request):
    return render(request,'message.html')