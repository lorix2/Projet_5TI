from random import randint

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group

from django.http import Http404
from django.shortcuts import render, redirect

from django.contrib import messages
from log.models import Person
from .forms import NameForm, class_form, add_classe_to_user, sub, add_exe


#view home avec tp
def home(request):

    return render(request,'index.html')

def sign_page(request):
    return render(request,'sign_page.html')

#view creation de compte eleve
def sing(request):
    try:
        form = NameForm(request.POST)
        user = form.data.get("username")
        sname = form.data.get("sname")
        fname = form.data.get("fname")
        mdp = form.data.get("mdp")

        if form.is_valid():
            random_n = randint(1,9999)
            g = Group.objects.get(name='eleve')
            user = User.objects.create_user(username=user, first_name=fname, last_name=sname, password=mdp)
            g.user_set.add(user)

    except Person.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'singup.html')

#view creation de compte prof
def sing_prof(request):
    try:
        form = NameForm(request.POST)
        user = form.data.get("username")
        sname = form.data.get("sname")
        fname = form.data.get("fname")
        mdp = form.data.get("mdp")

        if form.is_valid():
            random_n = randint(1,9999)
            g = Group.objects.get(name='prof')
            user = User.objects.create_user(username=user, first_name=fname, last_name=sname, password=mdp)
            g.user_set.add(user)
            user = authenticate(request, username=user, password=mdp)
            if user is not None and user.is_active:

                login(request, user)

    except Person.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'prof-singup.html')


#view une fois connecte
def log(request, username):

    return render(request, 'log.html')

#view de login
def loginn(request):
    try:

        if request.method == "POST":

            username = request.POST['username']
            password = request.POST['mdp']


            user = authenticate(request, username=username, password=password)

            if user is not None and user.is_active:
                name = request.user.username
                login(request, user)
                messages.success(request, name)
                l = request.user.groups.values_list('name', flat=True)
                l_as_list = list(l)
                print(request.user.username)

                if l_as_list[0] == "prof":
                    return redirect("/prof/"+request.user.username)
                if l_as_list[0] == "eleve":
                    return redirect("/eleve/"+request.user.username)

            else:
                print('error')

    except Person.DoesNotExist:
        raise Http404("Question does not exist")

    return render(request, 'login.html')

#view de prof pour la gestion des classes
def prof(request, username):

    users = User.objects.filter(groups__name='eleve')

    form = class_form(request.POST)
    form_ = add_classe_to_user(request.POST)# ajout de classe
    form2 = add_exe(request.POST)


    if form.is_valid():


        classe = form.data.get("c")

        Group.objects.create(name=classe)

    #selection des utilisatuer et attribution des classe au eleve
    if form_.is_valid():
        c_select = form_.data.get("c_select")
        answer = form_.data.get("se")
        user_s = User.objects.get(username=c_select).id
        print(c_select)


        g = Group.objects.get(name=answer)

        g.user_set.add(user_s)
    if form2.is_valid():
        tst = form2.data.get("exe_t")
        tt = form2.data.get("class_select")
        Person.objects.create(first_name=tst, last_name=tt)
        print(tst)
        print(tt)

    grp_classe = Group.objects.all()
    len_of_grp = len(grp_classe)-2
    classes_dic = {}
    classes = grp_classe[0:len_of_grp]

    for c in classes:


        user = users.filter(groups__name=c.name)
        u = user.values()

    return render(request,'log_prof.html', {"user": users, "classe": grp_classe[0:len_of_grp], "classes_user": User.objects.filter(groups__name="1D"), "e" : Person.objects.all()})

def eleve(request, username):

    user_cl = request.user.groups.all()
    len_of_grp = len(user_cl)
    classe_user = user_cl[1:len_of_grp]
    all_ex = Person.objects.all()
    exee = []
    for ex in all_ex:
        if ex.last_name == classe_user[0]:
            exee.append(ex.first_name)
    print(exee)
    form = sub(request.POST)

    mess = form.data.get("subin")
    print(mess)
    return render(request,'log_eleve.html', {"clas": classe_user, "exe": all_ex, "classs" : str(classe_user[0])})

@login_required
def deco(request):
    logout(request)
    return redirect('/login/')

def redirect_home(request):
    return redirect("/home")

def t(request):


    return render(request,'tp2.html')

def Unread(request):

  count=request.body['count']

  print("hello")

  print("count status ",count)