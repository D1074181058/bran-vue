from django import forms
from captcha.fields import CaptchaField


class signupform(forms.Form):
    Name = forms.CharField(max_length=10, initial='',widget=forms.TextInput(attrs={'placeholder': '吳宗翰'}))
    account = forms.CharField(max_length=20,initial='',)
    password = forms.CharField(max_length=20,initial='',widget=forms.PasswordInput)
    email = forms.EmailField(max_length=100, required=False,initial='')
    date = forms.DateField(required=False,widget=forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD'}))
    phone = forms.CharField(max_length=10, required=False,initial='')
    address = forms.CharField(max_length=47, required=False,initial='')


class loginform(forms.Form):
    account = forms.CharField(max_length=20, initial='')
    password = forms.CharField(max_length=20, initial='',widget=forms.PasswordInput)
    captcha = CaptchaField()