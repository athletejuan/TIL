from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm
from .forms import UserCustomChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

def signup(request):
    if request.user.is_authenticated:   # 인증된 유저가 요청을 보낸 경우, 회원가입 페이지를 보여주지 않고 목록 페이지로 redirect
        return redirect('articles:index')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)   # 회원가입 후 바로 로그인상태로 전환
            return redirect('articles:index')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/auth_form.html', {'form':form})

def login(request):
    if request.user.is_authenticated:   # 인증된 유저가 요청을 보낸 경우, 로그인 페이지를 보여주지 않고 목록 페이지로 redirect
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

def quit(request):
    if request.method == 'POST':
        request.user.delete()
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