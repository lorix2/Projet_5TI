from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#Formulaire creation de compte

class NameForm(forms.Form):
    username = forms.CharField(max_length=100)
    fname = forms.CharField(max_length=100)
    sname = forms.CharField(max_length=100)
    mdp = forms.CharField(max_length=100)

class userForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2'
        ]
#formulaire de gestion de classe
class class_form(forms.Form):
    c = forms.CharField(max_length=100)
#formulaire pour ajouter de classe

class add_classe_to_user(forms.Form):
    c_select = forms.CharField(max_length=100)
