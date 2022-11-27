from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import redirect
from django.contrib.auth.models import User



@csrf_protect
def user_login(request):
    return render(request, 'user_auth/login.html')

def authenticate_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is None:
        return HttpResponseRedirect(
            reverse('user_auth:register')
)
    else:
        login(request, user)
        return HttpResponseRedirect(
            reverse('user_auth:show_user')
        )    

def show_user(request):
    print(request.user.username)
    return render(request, 'user_auth/user.html', {
        "username": request.user.username,
        "password": request.user.password
    })   

def user_reg(request):
    return render(request, 'user_auth/register.html')

def register(request):
    username = request.GET['username']
    password = request.GET['password']
    user = User.objects.create_user(username, None, password)
    login(request, user)
    return HttpResponseRedirect(
            reverse('user_auth:show_user')
        )
    
    
	         
