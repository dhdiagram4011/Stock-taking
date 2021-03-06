from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView,LogoutView

## ..path
##localhost:8000/stock_member/myinfo
##....

urlpatterns = [
    path('register/', register, name='register'),
    path('register_success/', RegisterResult, name='RegisterResult'),
    ###path('login/', LoginView.as_view(template_name='stock_member/stock_login.html'), name='login'),
    path('login/', login, name='login'),
    path('logout/', LogoutView.as_view(template_name='stock_member/stock_logout.html'), name='logout'),
    path('userlist/', Userlist, name='Userlist'),
    path('login_success/', Login_success, name='Login_success'),
    path('home/', home, name='home'),
    path('myinfo/', myinfo, name='myinfo'),
    path('getout/', getout, name='getout'),
]