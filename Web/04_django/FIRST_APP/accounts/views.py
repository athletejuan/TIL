from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/index/')
    else:
        form = UserCreationForm()
        return render(request, 'accounts/signup.html', {'form':form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('/index/')
    else:
        form = AuthenticationForm()
        return render(request, 'accounts/login.html', {'form':form})