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
from django.contrib.auth.hashers import check_password


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



def login(request):
    if request.method == 'GET':
        return render(request, 'stock_member/stock_login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

    res_data = {}
    if not (username and password):
        res_data['error']  = "모든 정보를 정확히 입력하여 주세요"
    else:
        fuser = User.objects.get(username=username)

        if check_password(password, fuser.password):
            request.session['user'] = fuser.id
            return redirect('/home')
        else:
            res_data['error'] = "비밀번호가 맞지 않습니다"

    return render(request, 'stock_member/stock_login.html', res_data)


def home(request):
    user_pk = request.session.get('user')

    if user_pk:
        fuser = User.objects.get(pk=user_pk)
        return HttpResponse(fuser.username)

    return HttpResponse("로그인이 정상적으로 완료되었습니다")


#def login_success(request):
#    if request.method == 'GET':
#        return render(request, 'stock_member/stock_login_success.html')
#    elif request.method == 'POST':
#        username = request.POST.get('username')
#        password = request.POST.get('password')

#    res_data = {}
#    if not (username and password):
#        res_data['error']  = "모든 정보를 정확히 입력하여 주세요"
#    else:
#        fuser = User.objects.get(username=username)

#        if check_password(password, fuser.password):
#            request.session['user']=fuser.id

#            #return render(request, 'stock_member/stock_login_success.html')
#            return redirect('/home')
#        else:
#            res_data['error'] = "비밀번호가 맞지 않습니다"

#    return render(request, 'stock_member/stock_login.html', res_data)


@login_required()
def Userlist(request):
    userlists = User.objects.all()
    return render(request, 'stock_member/userlist.html', {'userlists':userlists})


def RegisterResult(request):
    userlists = User.objects.all().order_by('-id')[:1]
    return render(request, 'stock_member/stock_register_success.html', {'userlists':userlists})


