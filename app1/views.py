from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

def homepage(request):
    return render(request,'home.html')

def loginpage(request):
    if request.method=='POST':
        username=request.POST.get('username1')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse('username or password is incorrect')
    return render(request,'login.html')

# User Register
def signuppage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('usergmail')
        pass1=request.POST.get('userpassword')
        my_user=User.objects.create_user(uname,email,pass1)
        my_user.save()
        return redirect('login')

    return render(request,'signup.html')
