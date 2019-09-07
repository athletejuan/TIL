from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from .forms import UserCustomChangeForm, UserCustomCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash

def signup(request):
    if request.user.is_authenticated:   # 만약 로그인이 된 상태면 바로 index 페이지로 보냄
        return redirect('/boards/')
    if request.method == "POST":
        form = UserCustomCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request,user)
            return redirect('/boards/')
    else:
        form = UserCustomCreationForm()
    context = {'form':form}
    # return render(request, 'accounts/auth_form.html', context)
    return render(request, 'accounts/signup.html', context)

def login(request):
    if request.user.is_authenticated:   # 만약 로그인이 된 상태면 바로 index 페이지로 보냄
        return redirect('/boards/')
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or '/boards/')
    else:
        form = AuthenticationForm()
    context = {'form':form}
    return render(request, 'accounts/login.html', context)

def logout(request):
    if request.method == 'POST':
        auth_logout(request)
        return redirect('/boards/')
    else:
        return redirect('/boards/')

def delete(request):
    if request.method == 'POST':
        request.user.delete()
        return redirect('/boards/')
    else:
        return redirect('/boards/')

def edit(request):
    if request.method == 'POST':
        form = UserCustomChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/boards/')
    else:
        form = UserCustomChangeForm(instance=request.user)
    context = {'form':form}
    return render(request, 'accounts/edit.html', context)

def change_password(request):
    form = PasswordChangeForm(request.user, request.POST)
    if form.is_valid():
        user = form.save()
        update_session_auth_hash(request, user)
        form.save()
        return redirect('/boards/')
    else:
        form = PasswordChangeForm(request.user)
    context = {'form':form}
    return render(request, 'accounts/change_password.html', context)