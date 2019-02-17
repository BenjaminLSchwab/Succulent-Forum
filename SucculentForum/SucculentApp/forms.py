from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from SucculentApp.models import Topic

class SignUpForm(UserCreationForm):
    

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', )

class ThreadForm(forms.Form):
    title = forms.CharField(max_length=100)
    Body = forms.CharField()
    

    
