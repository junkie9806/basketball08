from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from login.forms import RegisterForm
from django.contrib.auth.models import User

def login_main(request):
    return render(request, 'login/login_main.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # 사용자 인증
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # 인증 성공 시 로그인 처리
            login(request, user)
            return redirect('core:home')  # 로그인 성공 시 홈으로 리디렉션
        
    return render(request, 'login/login_main.html')


def login_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            name = form.cleaned_data.get('name')
            phone_number=form.cleaned_data.get('phone_number')
            email=form.cleaned_data.get('email')
            address=form.cleaned_data.get('address')

            user = User.objects.create(username=username, phone_number=phone_number, email=email, address=address)
            user.set_password(password)
            user.name = name
            user.save()

            return render(request, 'login/success.html')
    else:
        form = RegisterForm() 
    
    return render(request, 'login/login_register.html', {'form': form})
