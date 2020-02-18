"""tcode URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework_swagger.views import get_swagger_view
from rest_framework.schemas.coreapi import AutoSchema
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token


admin.site.site_header = 'Inventory-information-collection-function & Join_memberShipAPI'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('testapp.urls')), #applicaton url
    path('join/', include('join_membership.urls')),
    path('api/doc/', get_swagger_view(title='serverlist api manual')), ##swagger api document url
    path('api/getToken/', views.obtain_auth_token),
    path('api/token/', obtain_jwt_token), ##토큰발급
]



