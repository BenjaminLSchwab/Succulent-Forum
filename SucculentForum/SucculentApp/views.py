from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from SucculentApp.forms import SignUpForm
from django.contrib.auth.forms import UserCreationForm
from SucculentApp.models import Profile
# Create your views here.

def index(request):
    return render(request, 'SucculentApp/index.html')

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES) #form contains info from the register page
        if form.is_valid():
            
            #fill out a userCreationForm and use it to create a user
            # userForm = UserCreationForm()
            # userForm.username = form.UserName
            # userForm.password1 = form.Password1
            # userForm.password2 = form.Password2
            # user = userForm.save()

            #screw that, lets actually create a user the right way

            user = User.objects.create_user(form.cleaned_data['UserName'], form.cleaned_data['Email'], form.cleaned_data['Password1'])

            profile = Profile()
            profile.User = user
            profile.Signature = form.cleaned_data['Signature']
            profile.Avatar = request.FILES['Avatar']
            profile.save()

            return render(request, 'SucculentApp/index.html')
        else:
            form = SignUpForm()
            return render(request, 'accounts/Register.html', {'form':form})

    else:
        form = SignUpForm()
        return render(request, 'accounts/Register.html', {'form':form})
