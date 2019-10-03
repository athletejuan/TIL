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
        if form.is_valid():
            # form.save()
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
        form = AuthenticationForm()
    return render(request, 'accounts/auth_form.html', {'form':form})

def logout(request):
    if request.method == 'POST':
        auth_logout(request)
        return redirect('articles:index')
    return redirect('articles:index')

def delete(request):
    if request.method == 'POST':
        request.user.delete()
    return redirect('articles:index')

def edit(request):
    if request.method == 'POST':
        # form = UserChangeForm(request.POST, instance=request.user)  공개되면 안되는 회원정보까지 보이는 문제
        form = UserCustomChangeForm(request.POST, instance=request.user) # forms.py 에서 email, first_name, last_name만 보이게 설정
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        # form = UserChangeForm(instance=request.user)
        form = UserCustomChangeForm(instance=request.user)
    return render(request, 'accounts/auth_form.html', {'form':form})

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            # form.save()
            user = form.save
            update_session_auth_hash(request, user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/auth_form.html', {'form':form})