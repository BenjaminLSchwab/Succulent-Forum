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

class PollForm(forms.Form):
    Title = forms.CharField(max_length=100, required=True)
    StartDate = forms.DateField(required=False) # set start date to now if not specified
    EndDate = forms.DateField(required=False) # if there is an end date, do not show results until end. If there is no end date, show results always

class ChoiceForm(forms.Form):
    Title = forms.CharField(max_length=100, required=True)

    
    

    
