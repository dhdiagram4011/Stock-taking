from django.utils import timezone
from django.shortcuts import redirect, render
from .forms import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404
from django.core.mail import EmailMessage

def mailer():
    userlists = User.objects.all().order_by('-id')[:1]
    title = "[제고관리시스템]제고관리 시스템 회원가입이 완료되었습니다."
    html_message = render_to_string('join_membership/register_result.html', {'userlists':userlists})
    email = EmailMessage(title, html_message, to=['rlaehgud21764011@gmail.com'])
    email.content_subtype = "html"
    return email.send()


@login_required
def document(request):
    return render(request, 'join_membership/document.html')


#회원가입
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            #userlist = User.objects.all().order_by('-id')[:1]
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            mailer()
        #return redirect('RegisterResult')
        return render(request, 'Join_membership/register_result.html')
    else:
        form = RegisterForm()
        return render(request, 'join_membership/register.html', {'form':form})


#회원가입
#def Register(request):
#    if request.method == 'POST':
#        form = RegisterForm(request.POST)
#        if form.is_valid():
#            posts = form.save()
#            username = request.POST.get('username', None)
#            password = request.POST.get('password', None)
#            repassword = request.POST.get('repassword', None)
#            email = request.POST.get('email', None)
#            created_date = request.POST.get('created_date', None)
#            published_date = request.POST.get('published_date', None)
#        return redirect('register_result')
#    else:
#        form = RegisterForm()
#        return render(request, 'join_membership/register.html', {'form': form})


#회원가입 결과
#def RegisterResult(request):
#    userlists = User.objects.all().order_by('-id')[:1]
#    return render(request, 'Join/register_result.html', {'userlists':userlists})

