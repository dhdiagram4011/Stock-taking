from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django import forms
from .models import *

class UserForm(forms.ModelForm):
    password = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='repassword', widget=forms.PasswordInput)

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('패스워드가 서로 같은지 확인해 주세요')
        return cd['password2']

    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','depart','position','phone','floor']


