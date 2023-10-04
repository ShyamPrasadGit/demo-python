from django.http import HttpResponse
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def demo(request):
     return render(request,'home.html')

