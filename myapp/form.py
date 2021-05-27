from django import forms
from captcha.fields import CaptchaField


class signupform(forms.Form):
    Name = forms.CharField(min_length=2,max_length=10, initial='',widget=forms.TextInput(attrs={'placeholder': '王小明(必填)','autocomplete':'off'}))
    account = forms.CharField(max_length=10,initial='',widget=forms.TextInput(attrs={'placeholder': '(必填)','autocomplete':'off'}))
    password = forms.CharField(max_length=20,initial='',widget=forms.PasswordInput(attrs={'placeholder': '(必填)','autocomplete':'off'}))
    email = forms.EmailField(max_length=100,initial='',widget=forms.TextInput(attrs={'placeholder': '(必填)','autocomplete':'off',}))
    date = forms.DateField(required=False,widget=forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD','autocomplete':'off'}))
    phone = forms.CharField(max_length=10, required=False,initial='',widget=forms.TextInput(attrs={'autocomplete':'off'}))
    address = forms.CharField(max_length=47, required=False,initial='',widget=forms.TextInput(attrs={'autocomplete':'off'}))





class loginform(forms.Form):
    account = forms.CharField(max_length=20, initial='',widget=forms.TextInput(attrs={'autocomplete':'off'}))
    password = forms.CharField(max_length=20, initial='',widget=forms.PasswordInput(attrs={'autocomplete':'off'}))
    captcha = CaptchaField()

class contactusform(forms.Form):
    Name = forms.CharField(max_length=10, initial='',widget=forms.TextInput(attrs={'placeholder': '吳宗翰','autocomplete':'off'}))
    phone = forms.CharField(max_length=20,initial='',widget=forms.TextInput(attrs={'autocomplete':'off'}))
    title = forms.CharField(max_length=50, required=False,initial='',widget=forms.TextInput(attrs={'autocomplete':'off'}))
    content = forms.CharField(required=False,initial='',widget=forms.TextInput(attrs={'autocomplete':'off'}))