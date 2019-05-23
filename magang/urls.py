"""magang URL Configuration

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
from django.urls import path
from DSSpgn import views as user_views
from django.contrib.auth import views as auth_views
import re as r

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_views.front, name='front'),
    path('ngagel/', user_views.dashboard, name='ngagel'),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='template/registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='template/registration/logout.html'), name='logout'),
    path('purwakarta/', user_views.dashboardpwkt, name='purwakarta'),
    path('jes/', user_views.dashboardjes, name='jes'),
    path('indogas/', user_views.dashboardindogas, name='indogas'),
    #----------------------------------Solusi-------------------------------------
    path(r'getidgtm/<id>', user_views.getidgtm, name='getidgtm'),
    path(r'getidgtmjes/<id>', user_views.getidgtmjes, name='getidgtmjes'),
    path(r'getidgtmindo/<id>', user_views.getidgtm, name='getidgtmindo'),
    path(r'getidgtmpur/<id>', user_views.getidgtmjes, name='getidgtmpur'),
    path(r'GTM/', user_views.GTM, name='GTM'),
    path(r'PRS/', user_views.PRS, name='PRS')
]
