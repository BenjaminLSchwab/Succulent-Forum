from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from SucculentApp.models import Topic

from django.contrib.auth.models import User

class SignUpForm(forms.Form):
    UserName = forms.CharField()
    Email = forms.EmailField()
    Password1 = forms.CharField(widget=forms.PasswordInput())
    Password2 = forms.CharField(widget=forms.PasswordInput())
    Signature = forms.CharField()
    Avatar = forms.ImageField()


class ThreadForm(forms.Form):
    title = forms.CharField(max_length=100)
    Body = forms.CharField()

class PostForm(forms.Form):
    Body = forms.CharField(max_length=10000, required=True)
    HasPoll = forms.BooleanField(required=False)

    
    

    
