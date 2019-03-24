from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from SucculentApp.forms import SignUpForm
from django.contrib.auth.forms import UserCreationForm
from SucculentApp.models import Profile
from SucculentApp.models import Thread, Topic
#from django.contrib.auth.forms import UserCreationForm
from SucculentApp.forms import UserCreationForm, ThreadForm
import datetime

# Create your views here.

def index(request):
    return render(request, 'SucculentApp/index.html')

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES) #form contains info from the register page
        if form.is_valid():
            if form.cleaned_data['Password1'] != form.cleaned_data['Password2']:
                errorText = "Passwords do not match."
                return render(request, 'accounts/Register.html', {'form':form, 'errorText':errorText})

            try:
                user = User.objects.create_user(form.cleaned_data['UserName'], form.cleaned_data['Email'], form.cleaned_data['Password1'])

            except:
                errorText = "Username / Email is already in use."
                return render(request, 'accounts/Register.html', {'form':form, 'errorText':errorText})


            profile = Profile()
            profile.User = user
            profile.Signature = form.cleaned_data['Signature']
            profile.Avatar = request.FILES['Avatar']
            profile.save()

            return redirect("/SucculentApp/")
            
        else:
            form = SignUpForm()
            return render(request, 'accounts/Register.html', {'form':form})

    else:
        form = SignUpForm()
        return render(request, 'accounts/Register.html', {'form':form})
        
        
def newThread(request, topic_id):
    if request.method == 'POST':
        form = ThreadForm(request.POST)
        if form.is_valid():
            topic = Topic.objects.filter(pk=topic_id)[0]
            user = User.objects.filter(pk=request.user.id)[0]
            NewThread = Thread(Title=form.data['title'],DateUpdated=datetime.datetime.today().strftime('%Y-%m-%d'),
            Body=form.data['Body'],TopicId=topic,
            UserId=user,DateStarted=datetime.datetime.today().strftime('%Y-%m-%d'),
            PostCount=0,
            ViewCount=1)
            NewThread.save()
            return HttpResponseRedirect(request.path_info)
        else: 
            return HttpResponse(str(form.errors))
    else:
        topic = Topic.objects.filter(pk=topic_id)
        user = User.objects.filter(pk=request.user.id)
        form = ThreadForm(initial={
            'DateUpdated':datetime.datetime.today().strftime('%Y-%m-%d'),
            'ViewCount':1,
            'TopicId':topic[0],
            'UserId': user[0],
            'DateStarted':datetime.datetime.today().strftime('%Y-%m-%d'),
            'PostCount':0
        })
        context = {
            'form': form
        }

    return render(request, 'SucculentApp/topicCreate.html', context)

def newPost(request, thread_id):
    if request.method == 'POST':
       
    else:
       
        context = {
            'form': form
        }

    return render(request, 'SucculentApp/topicCreate.html', context)