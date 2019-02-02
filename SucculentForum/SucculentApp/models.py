from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    Signature = models.CharField(null=True, max_length=200)
    Avatar = models.CharField(max_length=500)

class Topic(models.Model):
    Title = models.CharField(max_length=50)
    DateUpdated = models.DateField()
    ThreadCount = models.IntegerField()

class Thread(models.Model):
    Title = models.CharField(max_length=50)
    DateUpdated = models.DateField()
    Body = models.CharField(max_length=10000)
    UserId = models.ForeignKey(User, on_delete=models.CASCADE)
    ViewCount = models.IntegerField()
    TopicId = models.ForeignKey(Topic, on_delete=models.CASCADE)
    DateStarted = models.DateField()
    PostCount = models.IntegerField()

class Poll(models.Model):
    Title = models.CharField(max_length=50)
    StartDate = models.DateField()
    EndDate = models.DateField()

class Post(models.Model):
    PollId = models.ForeignKey(Poll, null=True, on_delete=models.CASCADE)
    Body = models.CharField(max_length=10000)


class Choice(models.Model):
    PollId = models.ForeignKey(Poll, on_delete=models.CASCADE)
    VoteCount = models.IntegerField()

class Vote(models.Model):
    PollId = models.ForeignKey(Poll, on_delete=models.CASCADE)
    UserId = models.ForeignKey(User, on_delete=models.CASCADE)

class Message(models.Model):
    Title = models.CharField(max_length = 50)
    Body = models.CharField(max_length = 10000)
    DateSent = models.DateField()
    DateRead = models.DateField(null = True)
    SenderId = models.ForeignKey(User, null= True, on_delete=models.CASCADE)

class MessageRecipientLink(models.Model):
    MesageId = models.ForeignKey(Message, on_delete=models.CASCADE)
    UserId = models.ForeignKey(User, on_delete=models.CASCADE)
