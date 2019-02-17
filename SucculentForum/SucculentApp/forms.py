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
    DateUpdated = forms.DateField(widget = forms.HiddenInput(),required=False)
    Body = forms.CharField()
    UserId = forms.ModelChoiceField(queryset=User.objects.all(),widget=forms.HiddenInput(),required=False)
    ViewCount = forms.IntegerField(widget=forms.HiddenInput(),required=False)
    TopicId = forms.ModelChoiceField(queryset=Topic.objects.all(),widget=forms.HiddenInput(),required=False)
    DateStarted = forms.DateField(widget = forms.HiddenInput(),required=False)
    PostCount = forms.IntegerField(widget=forms.HiddenInput(),required=False)
    

    
