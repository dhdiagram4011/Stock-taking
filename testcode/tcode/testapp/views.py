from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import redirect, render
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.core import serializers
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

def Sendmail():
    serverlists = Serverlist.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:1]
    title = "[제고등록]제고가 아래와 같이 등록되었습니다."
    html_message = render_to_string('testapp/serverlist_result.html', {'serverlists':serverlists})
    email = EmailMessage(title, html_message, to=['rlaehgud21764011@gmail.com'])
    email.content_subtype = "html"
    return email.send()

def Listall():
    serverlists = Serverlist.objects.all()
    title = "[제고리스트]제고리스트 이메일 발송성공."
    html_message = render_to_string('testapp/serverlist_all.html', {'serverlists':serverlists})
    email = EmailMessage(title, html_message, to=['rlaehgud21764011@gmail.com'])
    email.content_subtype = "html"
    return email.send()

##권힌속성
from .permissions import *


## 로그인 하지 않으면 페이지 접근 불가
###@login_required
def serverlist(request):
    if request.method == 'POST':
        form = ServerlistForm(request.POST)
        if form.is_valid():
            posts = form.save()
            name = request.POST.get('name', None)
            server_count = request.POST.get('server_count',None)
            model_name = request.POST.get('model_name', None)
            code = request.POST.get('code', None)
            use_case = request.POST.get('use_case',None)
            created_date =  request.POST.get('created_date', None)
            published_date = request.POST.get('published_date' , None)
            Sendmail()
        return redirect('serverlist_result')
    else:
        if not request.user.is_authenticated:
            return render(request, 'testapp/need_login.html')
        else:
            form = ServerlistForm()
            return render(request, 'testapp/serverlist.html', {'form':form})



## 로그인 하지 않으면 페이지 접근 불가
@login_required
def serverlist_result(request):
    serverlists = Serverlist.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:1]
    return render(request, 'testapp/serverlist_result.html', {'serverlists':serverlists})


## 서버 전체 리스트를 이메일로 보내기
## 로그인 하지 않으면 페이지 접근 불가
## 등록된 제고 전체를 볼 수 있는 페이지 /serverlist_all
@login_required
def serverlist_all(request):
    serverlists = Serverlist.objects.all()
    Listall() ###send_mail로 이메일 발송
    return render(request, 'testapp/serverlist_all.html', {'serverlists':serverlists})



@api_view(['GET'])
@permission_classes((IsAuthenticated,))
@authentication_classes((JSONWebTokenAuthentication,))
def serverall(request):
    serverlists = Serverlist.objects.all()
    serverlisting = serializers.serialize('json',serverlists)
    return HttpResponse(serverlisting, content_type="text/json-comment-filtered")



### API 접근 - API를 이용하여 서버 리스트를 보여줌
from rest_framework import generics
from .models import *
from .serializers import ServerlistSerializer


## 로그인 하지 않으면 json기반 서버 리스트 목록 볼 수 없음
class ServerList(LoginRequiredMixin, generics.ListCreateAPIView):
    queryset = Serverlist.objects.all()
    serializer_class = ServerlistSerializer

## 로그인 하지 않으면 json기반 서버 리스트 목록 볼 수 없음
class ServerlistDetail(LoginRequiredMixin, generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication,) ##토큰방식 인증
    permission_classes = (IsAuthenticated,IsOwnerOrReadOnly) ##인증을 해야만 볼 수 있는 페이지
    queryset = Serverlist.objects.all()
    serializer_class = ServerlistSerializer













