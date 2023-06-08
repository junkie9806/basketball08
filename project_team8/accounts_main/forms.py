from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    # 추가 필드를 위한 폼 필드 정의
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=20)
    address = forms.CharField(max_length=100)

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'password1', 'password2', 'first_name', 'email', 'phone_number', 'address')