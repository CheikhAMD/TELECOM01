from django.shortcuts import render
from . models import *
# Create your views here.

def main(request):
    return render(request,'user/main.html')


def home(request):
    return render(request,'user/home.html')


def bouti_01(request):
    return render(request,'user/bouti_01.html')

def bouti_02(request):
    return render(request,'user/bouti_02.html')


def bouti_03(request):
    return render(request,'user/bouti_03.html')


def bouti_04(request):
    return render(request,'user/bouti_04.html')


def about(request):
    return render(request,'user/about.html')