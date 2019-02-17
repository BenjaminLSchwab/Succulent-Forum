from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from SucculentApp.models import Thread, Topic
#from django.contrib.auth.forms import UserCreationForm
from SucculentApp.forms import UserCreationForm, ThreadForm
import datetime

# Create your views here.

def index(request):
    return render(request, 'SucculentApp/index.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
    else:
        form = UserCreationForm()
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