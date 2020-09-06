from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login

import random
# Create your views here.

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

def currenttodos(request):
    return render(request, 'todo/currenttodos.html',{'current':"Welcome To Your Current TO Do's"})

