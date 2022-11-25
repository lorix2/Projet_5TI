"""MYapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, Group
from django.http import Http404, HttpResponseRedirect, request
from django.shortcuts import render, redirect
from django.urls import reverse

from log.models import Person
from .forms import NameForm
from MYapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sinup/eleve', views.sing),
    path('sinup/prof', views.sing_prof),
    path('login/', views.loginn),
    path('log', views.log, name='log'),
    path('eleve/<str:username>', views.eleve, name='log'),
    path('prof/<str:username>', views.prof, name='log'),
    path('logout', views.deco, name="logout"),
    path('home', views.home, name='home'),
    path('', views.redirect_home, name='redirect_home')


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
