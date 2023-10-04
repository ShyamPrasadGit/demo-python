from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def login(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('form.html')
        else:
            messages.info(request,"Invalid credentials")
            return render(request,'home.html')
    return render(request,'login.html')
def register(request):
    if request.method == 'POST':
        username=request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already exist")
                return redirect('register')
            else:
                 user=User.objects.create_user(username=username,password=password)
                 user.save();
                 return redirect('login.html')
                 # messages.info(request,"User created successfully")
        else:
            messages.info(request,"Password not matching")
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

def form1(request):
    return render(request,'form.html')