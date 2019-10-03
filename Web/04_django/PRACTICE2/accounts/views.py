from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm
from .forms import UserCustomChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        user = form.save()
        auth_login(request, user)
        return redirect('articles:index')
    else:
        form = UserCreationForm()
        return render(request, 'accounts/auth_form.html', {'form':form})

def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm(request)
        return render(request, 'accounts/auth_form.html', {'form':form})

def logout(request):
    if request.method == 'POST':
        auth_logout(request)
        return redirect('articles:index')
    return redirect('articles:index')

def edit(request):
    if request.method == 'POST':
        form = UserCustomChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = UserCustomChangeForm(instance=request.user)
        return render(request, 'accounts/auth_form.html', {'form':form})

def delete(request):
    if request.method == 'POST':
        request.user.delete()
        return redirect('articles:index')
    return redirect('articles:index')

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/auth_form.html', {'form':form})
    