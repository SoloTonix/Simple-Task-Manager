from django.shortcuts import render, redirect
from . forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.
def Register(request):
    form = RegisterUserForm()
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Accounts created, Now you can login')
            return redirect('Login')

        else:
            messages.warning(request, 'Sorry, something went wrong fg')
            return redirect('Register')
        
    else:
        form = RegisterUserForm()
        messages.warning(request, 'Sorry, something went wrong')

    context = {'form':form}
    return render(request, 'users/register.html', context)
    
def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_active:
            login(request, user)
            return redirect('home')
        
        else:
            messages.error(request, 'Sorry something went wrong')
            return redirect('login')
    
    else:
        return render(request, 'users/login.html')


def Logout(request):
    logout(request)
    return redirect('Login')


