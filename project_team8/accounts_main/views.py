from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:accounts_main:user_login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts_main/signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')  # 로그인 후 이동할 URL
        else:
            error_message = '아이디 또는 패스워드가 올바르지 않습니다.'
            return render(request, 'accounts_main/login.html', {'error_message': error_message})
    else:
        return render(request, 'accounts_main/login.html')

def user_logout(request):
    logout(request)
    return redirect('/')  # 로그아웃 후 이동할 URL