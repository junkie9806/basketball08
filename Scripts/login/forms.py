from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=20, label='ID')
    password = forms.CharField(widget=forms.PasswordInput(), label='Password')
    name = forms.CharField(label='Name', max_length=100)
    phone_number = forms.CharField(max_length=11, label='Phone Number')
    email = forms.EmailField(label='Email')
    address = forms.CharField(max_length=100, label='Address')
