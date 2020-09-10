from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

import random
# Create your views here.

def home(request):
    return render(request, 'todo/home.html')

def signupuser(request):
    if request.method=='GET':
        return render(request, 'todo/signupuser.html', )
    else:
        if request.POST['password1']==request.POST['password2']:
            user=User.objects.create_user(request.POST['username'],request.POST['password1'])
            user.save() ###Save Record In Admin panel
            login(request,user)
            return redirect('currenttodos')
        else:
            return render(request, 'todo/signupuser.html',{'error':"Password Does't Match."} )

def loginuser(request):
    print("55555555555555555")
    if request.method=="GET":
        return render(request, 'todo/loginuser.html')
    else:
        print("2222")
        user=authenticate(request,username=request.POST['username'],pwd=request.POST['password'])
        print("ggg",user)
        if user is None:
            return render(request, 'todo/loginuser.html',{'error':"User name Or Password Does't Match" })
        else:
            login(request, user)
            return redirect('loginuser')



def currenttodos(request):
    return render(request, 'todo/currenttodos.html',{'current':"Welcome To Your Current TO Do's"})

def logoutuser(request):
    if request.method=='POST':
        logout(request)
        return redirect('home')


