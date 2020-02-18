from django.utils import timezone
from django.shortcuts import redirect, render
from .forms import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required


@login_required
def document(request):
    return render(request, 'join_membership/document.html')


#회원가입
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
        return render(request, 'join_membership/register_result.html', {'new_user':new_user})
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
#def register_result(request):
#    registers = Register.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:1]
#    return render(request, 'join_membership/register_result.html', {'registers':registers})

