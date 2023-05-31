from django.shortcuts import render, redirect
from .models import User
from django.http import HttpResponse
from .forms import LoginForm
from django.contrib.auth.hashers import make_password, check_password

def register(request):
    if request.method == 'GET':
        return render(request, 'accounts1/register.html')

    elif request.method == 'POST':
        username = request.POST.get('username', None)
        useremail = request.POST.get('useremail', None)
        phone = request.POST.get('phone', None)
        address = request.POST.get('address', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re_password', None)
        
        err_data={}
        if not(username and useremail and phone and address and password and re_password):
            err_data['error'] = '모든 값을 입력해주세요.'
        
        elif password != re_password:
            err_data['error'] = '비밀번호가 다릅니다.'
        
        else:
            user = User(
                username=username,
                useremail=useremail,
                phone = phone,
                address = address,
                password=make_password(password),
            )
            user.save()
            return redirect('main:accounts1:login')

        return render(request, 'accounts1/register.html', err_data)

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            request.session['user'] = form.user_id
            return redirect('/')
    else:
        form = LoginForm()
    return render(request, 'accounts1/login.html', {'form': form})
    
def logout(request):
    if request.session.get('user'):
        del(request.session['user'])
    return redirect('/')

