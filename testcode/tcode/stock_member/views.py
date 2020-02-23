from django.utils import timezone
from django.shortcuts import redirect, render, HttpResponse
from .forms import *
from django.contrib.auth.decorators import login_required
import smtplib
from .models import *

from django.core.mail import send_mail
from django.utils.html import strip_tags
from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404
from django.core.mail import EmailMessage

def mailer():
    userlists = User.objects.all().order_by('-id')[:1]
    title = "[제고관리시스템]제고관리 시스템 회원가입이 완료되었습니다."
    html_message = render_to_string('stock_member/stock_register_success.html', {'userlists':userlists})
    #email = EmailMessage(title, html_message, to=['rlaehgud21764011@gmail.com'])
    email = EmailMessage(title, html_message, to=['rlaehgud21764011@gmail.com'])
    email.content_subtype = "html"
    return email.send()



def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            userlists = User.objects.all().order_by('-id')[:1]
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            mailer()
        return redirect('RegisterResult')
    else:
        form = UserForm()
        return render(request, 'stock_member/stock_register.html', {'form':form})


@login_required()
def login_success(request):
    return render(request, 'stock_member/stock_login_success.html')


@login_required()
def Userlist(request):
    userlists = User.objects.all()
    return render(request, 'stock_member/userlist.html', {'userlists':userlists})


def RegisterResult(request):
    userlists = User.objects.all().order_by('-id')[:1]
    return render(request, 'stock_member/stock_register_success.html', {'userlists':userlists})


