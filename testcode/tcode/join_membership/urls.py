from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns  = [
    path('document/', document, name='document'), ##현 과제에 대한 설명
    path('login/', LoginView.as_view(template_name='join_membership/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='join_membership/logout.html'), name='logout'),
    path('register/', register, name='register'),
    #path('register_success/', RegisterResult, name='RegisterResult'),
]

