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
from django.contrib.auth import login, authenticate
from django.contrib import auth

## 회원가입 후 메일 발송처리
def mailer():
    userlists = User.objects.all().order_by('-id')[:1]
    title = "[제고관리시스템]제고관리 시스템 회원가입이 완료되었습니다."
    html_message = render_to_string('stock_member/stock_register_success.html', {'userlists':userlists})
    email = EmailMessage(title, html_message, to=['rlaehgud21764011@gmail.com'])
    email.content_subtype = "html"
    return email.send()


## 회원가입
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


# 쿠키기반 로그인
#def login(request):
#    if request.COOKIES.get('username') is not None:
#        username = request.COOKIES.get('username')
#        password = request.COOKIES.get('password')
#        user = auth.authenticate(request, username=username, password=password)
#        if user is not None:
#            auth.login(request, user)
#            return redirect('/stock_member/home')
#        else:
#            return render(request, "stock_member/stock_login.html")

#    elif request.method == "POST":
#        username = request.POST["username"]
#        password = request.POST["password"]
#        user = auth.authenticate(request, username=username, password=password)

#        if user is not None:
#            auth.login(request, user)
#            if request.POST.get("keep_login") == "TRUE":
#                response = render(request, 'stock_member/stock_login_success.html')
#                response.set_cookie('username' , username)
#                response.set_cookie('password' , password)
#                return response
#            return redirect("/stock_member/home")
#        else:
#            return render(request, 'stock_member/stock_login_err_msg.html')
#    else:
#        form = LoginForm()
#        return render(request, 'stock_member/stock_login.html', {'form':form})
#    return render(request, 'stock_member/stock_login.html')




###세션기반 로그인 인증
def login(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'stock_member/stock_login.html', {'form':form})
    elif request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]

    res_data = {}
    if not (username and password):
        res_data['error']  = "모든 정보를 정확히 입력하여 주세요"
    else:
        fuser = User.objects.get(username=username)
        #fuser = User.objects.all()

        if check_password(password, fuser.password):
            request.session['username'] = fuser.id
            return redirect('/stock_member/home')
        else:
            res_data['error'] = "비밀번호가 맞지 않습니다"

    return render(request, 'stock_member/stock_login.html', res_data)


def home(request):
    user_pk = request.session['username']

    if user_pk:
        fuser = User.objects.get(pk=user_pk)
        return HttpResponse(
            fuser.username + "님 사이트 방문을 환영합니다"'<br/>'
            '<br/>'
            '<a class ="" href="/stock_member/logout"> <strong>로그아웃하기</strong></a><br/>'
            '<a class ="" href="/"><strong>제고입력바로가기</strong></a><br/>'
            '<a class ="" href="/stock_member/myserver" > <strong> 나의 제고현황 보기</strong></a><br/>'
            '<a class ="" href="/stock_member/myinfo" > <strong>개인정보바로가기</strong></a><br/>'


        )
        #return render(request, 'stock_member/stock_login_success.html')
    else:
        #return HttpResponse("로그인이 정상적으로 완료되었습니다")
        return render(request, 'stock_memeber/stock_login_success.html')

## 나의정보 바로가기
def myinfo(request):
    myprofile_pk = request.session['username']

    if myprofile_pk:
        myprofile = User.objects.get(pk=myprofile_pk)
        return HttpResponse(
            "아이디 :  " + myprofile.username + '<br/>'
            "이메일 :  " + myprofile.email + '<br/>'
            "부서 :  " + myprofile.depart + '<br/>'
            "연락처 :  " + myprofile.phone + '<br/>'
            "근무층수 :  " + str(myprofile.floor) + '<br/>'
            "직책 : " + myprofile.position + '<br/>'
            "성 : " + myprofile.first_name + '<br/>'
            "이름 : " + myprofile.last_name + '<br/>'

        )

#def save_session(request, username, password):
#    request.session['username'] = username
#    request.session['password'] = password


#def login(request):
#   if request.method == 'POST':
#        username = request.sesison.get('username')
#        password = request.session.get('password')
#        save_session(request, username, password)
#        return render(request, 'stock_member/stock_login_success.html')
#   else:
#        form = LoginForm()
#        return render(request, 'stock_member/stock_login.html', {'form':form})


@login_required()
def Userlist(request):
    userlists = User.objects.all()
    return render(request, 'stock_member/userlist.html', {'userlists':userlists})


def RegisterResult(request):
    userlists = User.objects.all().order_by('-id')[:1]
    return render(request, 'stock_member/stock_register_success.html', {'userlists':userlists})


@login_required()
def Login_success(request):
    userlists = User.objects.all().order_by('-id')[:1]
    return render(request, 'stock_member/stock_login_success.html', {'userlists':userlists})

