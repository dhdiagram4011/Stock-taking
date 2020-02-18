from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django import forms
from .models import *

class RegisterForm(forms.ModelForm):
    password = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='repassword', widget=forms.PasswordInput)

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('패스워드가 서로 틀립니다! 재확인 해주세요')
        return cd['password2']

    class Meta:
        model = get_user_model()
        fields = ['username','first_name','last_name','email']


#회원가입 폼
#class RegisterForm(forms.ModelForm):
#    password = forms.CharField(label='password', widget=forms.PasswordInput)
#    repassword = forms.CharField(label='reconfirm password', widget=forms.PasswordInput)

#    class Meta:
#        model = Register
#        fields = ['id','username','email','password','repassword','created_date','published_date']

#    def clean_repassword(self):
#        cd = self.cleaned_data
#        if cd['password'] != cd['repassword']:
#            raise forms.ValidationError('Passwords do not match!')
#        return cd['repassword']


#로그인 폼
#class LoginForm(forms.ModelForm):
#    email = forms.CharField(label='email')
#    password = forms.CharField(label='password' , widget=forms.PasswordInput)

#    class Meta:
#        model = Login
#        fields = ['email','password']







