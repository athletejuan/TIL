from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm
from .forms import UserCustomChangeForm, UserCustomCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash

def signup(request):
    if request.user.is_authenticated:       # 만약 로그인이 된 상태이면 바로 index 페이지로 보냄
        return redirect('board:index')
    if request.method == 'POST':
        form = UserCustomCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('board:index')
    else:
        form = UserCustomCreationForm()
    context = {'form':form}
    return render(request, 'accounts/auth_form.html', context)

def login(request):
    if request.user.is_authenticated:       # 만약 로그인이 된 상태이면 바로 index 페이지로 보냄
        return redirect('board:index')
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'board:index')
    else:
        form = AuthenticationForm()
    context = {'form':form}
    return render(request, 'accounts/login.html', context)

def logout(request):
    if request.method == 'POST':
        auth_logout(request)
        return redirect('board:index')
    else:
        return redirect('board:index')

def delete(request):
    if request.method == 'POST':
        request.user.delete()
        return redirect('board:index')
    else:
        return redirect('board:index')

def edit(request):
    if request.method == 'POST':
        form = UserCustomChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('board:index')
    else:
        form = UserCustomChangeForm(instance=request.user)
    context = {'form': form}
    return render(request, 'accounts/auth_form.html', context)

def change_password(request):
    form = PasswordChangeForm(request.user, request.POST)
    if form.is_valid():
        user = form.save()
        update_session_auth_hash(request, user)   # 비밀번호가 변경되어도 '나'라고 알림
        form.save()
        return redirect('board:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {'form': form}
    return render(request, 'accounts/auth_form.html', context)