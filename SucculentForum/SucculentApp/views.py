from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import login, authenticate
#from django.contrib.auth.forms import UserCreationForm
from SucculentApp.forms import SignUpForm
# Create your views here.

def index(request):
    return render(request, 'SucculentApp/index.html')

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

    else:
        form = SignUpForm()
        return render(request, 'accounts/Register.html', {'form':form})
