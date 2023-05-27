from django.shortcuts import render, redirect
from .models import User
import json
from django.template import loader



# Create your views here.
def login_main(request):
    users = User.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User(request,user_id=username,password=password)
        if user is not None:
            return redirect('main:home')
        else:
            error_message = '아이디 또는 비밀번호가 올바르지 않습니다.'
            return render(request, 'login/login_main.html')
    return render(request, 'login/login_main.html', {'users' : users})

def login_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        name = request.POST['name']
        phone_number = request.POST['phone_number']
        email = request.POST['email']
        address = request.POST['address']
        user = User(username=username,password=password,name=name,phone_number=phone_number,email=email,address=address)
        user.save()
        return redirect('main:login:login_register')
    return render(request, 'login/login_register.html')

#def login_registering(request):
    if request.method == 'POST':
        form = User(request.POST)
        if form.is_valid():
            form.save()
            user_id = form.cleaned_data.get('user_id')
            password = form.cleaned_data.get('password')
            name = form.cleaned_data.get('name')
            phone_number=form.cleaned_data.get('phone_number')
            email=form.cleaned_data.get('email')
            address=form.cleaned_data.get('address')

            user = User.objects.create(user_id, phone_number, email, address)
            user.set_password(password)
            user.name = name
            user.save()

            return render(request, 'login/login_main.html')
    else:
        form = User() 
    
    return render(request, 'login/login_register.html', {'form': form})

def index(request):
    _context = {'check':False}
    if request.session.get('access_token'):
        _context['check'] = True
    return render(request, 'login_main.html', _context)

def kakaoLoginLogic(request):
    _restApiKey = '564eabed437df94a09f01adbce9cdbee' # 입력필요
    _redirectUrl = 'http://127.0.0.1:8000/kakaoLoginLogicRedirect'
    _url = f'https://kauth.kakao.com/oauth/authorize?client_id={"564eabed437df94a09f01adbce9cdbee"}&redirect_uri={"http://127.0.0.1:8000/kakaoLoginLogicRedirect/"}&response_type=code'
    return redirect(_url)

def kakaoLoginLogicRedirect(request):
    _qs = request.GET['code']
    _restApiKey = '564eabed437df94a09f01adbce9cdbee' # 입력필요
    _redirect_uri = 'http://127.0.0.1:8000/kakaoLoginLogicRedirect'
    _url = f'https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={"564eabed437df94a09f01adbce9cdbee"}&redirect_uri={"http://127.0.0.1:8000/kakaoLoginLogicRedirect/"}&code={_qs}'
    _res = request.post(_url)
    _result = _res.json()
    request.session['access_token'] = _result['access_token']
    request.session.modified = True
    return render(request, 'loginSuccess.html')

def kakaoLogout(request):
    _token = request.session['access_token']
    _url = 'https://kapi.kakao.com/v1/user/logout'
    _header = {
      'Authorization': f'bearer {_token}'
    }
    # _url = 'https://kapi.kakao.com/v1/user/unlink'
    # _header = {
    #   'Authorization': f'bearer {_token}',
    # }
    _res = request.post(_url, headers=_header)
    _result = _res.json()
    if _result.get('id'):
        del request.session['access_token']
        return render(request, 'loginoutSuccess.html')
    else:
        return render(request, 'logoutError.html')