from django.urls import path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns  = [
    path('', serverlist, name='serverlist'),
    path('serverall/', serverall, name='serverall'),
    path('serverlist_result/', serverlist_result, name='serverlist_result'),
    path('serverlist_all/', serverlist_all, name='serverlist_all'),
    path('serverlisting/', ServerList.as_view()),
    path('serverlisting/<int:pk>/', ServerlistDetail.as_view()),
    ##path('need_login/', need_login, name='need_login'),
    path('myserver/', MyServer, name='MyServer'),
]

