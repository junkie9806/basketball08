from django.shortcuts import render
from .models import User




# Create your views here.
def login_main(request):
    return render(request, 'login/login_main.html')

def login_register(request):
    return render(request, 'login/login_register.html')

def login_registering(request):
    if request.method == 'POST':
        form = User(request.POST)
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

            return render(request, 'login/login_main.html')
    else:
        form = User() 
    
    return render(request, 'login/login_register.html', {'form': form})
