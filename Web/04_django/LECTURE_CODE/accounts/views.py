from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm
from .forms import UserCustomChangeForm, UserCustomCreationForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model

def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method == "POST":
        form = UserCustomCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = UserCustomCreationForm()
    return render(request, 'accounts/auth_form.html', {'form':form})

def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form':form})

def logout(request):
    if request.method == "POST":
        auth_logout(request)
    return redirect('articles:index')

def delete(request):
    if request.method == "POST":
        request.user.delete()
    return redirect('articles:index')

def edit(request):
    if request.method == "POST":
        form = UserCustomChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = UserCustomChangeForm(instance=request.user)
    return render(request, 'accounts/auth_form.html', {'form':form})

def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/auth_form.html', {'form':form})

def profile(request, username):
    person = get_object_or_404(get_user_model(), username=username)
    if request.method == 'POST':
        return render(request, 'accounts/profile.html', {'person':person})
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form':form})