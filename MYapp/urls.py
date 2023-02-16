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
from django.urls import path

from MYapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls), #url interface admin
    path('sinup/eleve', views.sing, name="e"), #url sign up eleve
    path('sinup/prof', views.sing_prof, name="p"), # url sign up prof
    path('login/', views.loginn, name="login"), #url login
    path('log', views.log, name='log'), # url une fois connecté
    path('eleve/<str:username>', views.eleve, name='log'), # url une fois connecté eleve
    path('prof/<str:username>', views.prof, name='log'), # url une fois connecté prof
    path('logout', views.deco, name="logout"), #url de log out
    path('home', views.home, name='home'), #url home
    path('', views.redirect_home, name='redirect_home'), #url redirect vers home
    path('tp', views.t, name='tp'), #url home
    path('notification',views.Unread,name='Unread'),
    path('signup', views.sign_page, name='sp'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)# ajout des fichier static pour les templates
