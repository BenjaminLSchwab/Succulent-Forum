from django import forms

from django.contrib.auth.models import User

class SignUpForm(forms.Form):
    UserName = forms.CharField()
    Email = forms.EmailField()
    Password1 = forms.CharField(widget=forms.PasswordInput())
    Password2 = forms.CharField(widget=forms.PasswordInput())
    Signature = forms.CharField()
    Avatar = forms.ImageField()
