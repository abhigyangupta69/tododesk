from django.contrib import auth
from django.db import IntegrityError
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from pygame import mixer
from .forms import TodoForm
from .models import Todo
from django.shortcuts import render,get_object_or_404

import random
# Create your views here.

def home(request):
    return render(request, 'todo/home.html')

def signupuser(request):
    if request.method=='GET':
        return render(request, 'todo/signupuser.html',{'form':UserCreationForm()})
    else:
        if request.POST['password1']==request.POST['password2']:
            try:
                user=User.objects.create_user(request.POST['username'],request.POST['password1'])
                user.save() ###Save Record In Admin panel
                login(request,user)
                return redirect('currenttodos')
            except IntegrityError:
                return render(request, 'todo/signupuser.html', {'error1': "User Name Already Exist..."})
        else:
            file='/home/abhigyan/Downloads/abhigyan-you-just-received-a-text-message.mp3'
            mixer.init()
            mixer.music.load(file)
            mixer.music.play()
            return render(request, 'todo/signupuser.html',{'error':"Password Does't Match.",'form':UserCreationForm()})

def loginuser(request):
    if request.method=="GET":
        return render(request, 'todo/loginuser.html',{'form':AuthenticationForm()})
    else:
        a = request.POST['loginusername']
        b = request.POST['loginuserpassword']
        print(a,b)
        user = auth.authenticate(username=a,email=b)
        print("ggg",user)
        if user is None:
            return render(request, 'todo/loginuser.html',{'error':"User name Or Password Does't Match",'form':AuthenticationForm()})
        else:
            auth.login(request,user)
            return redirect('currenttodos')


def currenttodos(request):
    # todo_obj=Todo.objects.all()
    todo_obj=Todo.objects.filter(user=request.user)###It will show current login user Todo

    return render(request, 'todo/currenttodos.html',{'current':"Welcome To Your Current TO Do's",'todos':todo_obj})


def createtodos(request):
    if request.method=='GET':
        return render(request, 'todo/createtodos.html',{'form':TodoForm()})
    else:
        try:
            form=TodoForm(request.POST)
            newtodo=form.save(commit=False)
            newtodo.user = request.user
            newtodo.save()
            return redirect('currenttodos')
        except ValueError:
            return render(request, 'todo/createtodos.html', {'form': TodoForm()})


def logoutuser(request):
    if request.method=='POST':
        logout(request)
        return redirect('home')


def view_todo(request,todo_id):
    todo=get_object_or_404(Todo,pk=todo_id)###if Todo Id not available in Db Will give 404 error
    form=TodoForm(instance=todo)
    return render(request,'todo/view_todo.html',{'todo':todo,'form':form})