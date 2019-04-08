from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# profile has one to one relationship with user, is used as an extension of user
class Profile(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    #on_delete=models.CASCADE 
    #this means the profile will be deleted if the referenced user is deleted
    Signature = models.CharField(null=True, max_length=200)
    Avatar = models.ImageField()

class Topic(models.Model):
    Title = models.CharField(max_length=50)
    DateUpdated = models.DateField()
    ThreadCount = models.IntegerField()

class Thread(models.Model):
    Title = models.CharField(max_length=50)
    DateUpdated = models.DateField()
    Body = models.CharField(max_length=10000)
    UserId = models.ForeignKey(User, null=True, on_delete=models.SET_NULL) #nullable and non cascade delete so that we can archive old threads even if people leave the site
    ViewCount = models.IntegerField()
    TopicId = models.ForeignKey(Topic, on_delete=models.CASCADE)
    DateStarted = models.DateField()
    PostCount = models.IntegerField()

class Poll(models.Model):
    Title = models.CharField(max_length=50)
    StartDate = models.DateField()
    EndDate = models.DateField(null=True)

class Post(models.Model):
    ThreadId = models.ForeignKey(Thread, on_delete=models.CASCADE)
    PollId = models.ForeignKey(Poll, null=True, on_delete=models.SET_NULL)#deleting a poll should not delete the post it lived on
    Body = models.CharField(max_length=10000)

# A choice represents one of the options in the poll
class Choice(models.Model):
    PollId = models.ForeignKey(Poll, on_delete=models.CASCADE)
    VoteCount = models.IntegerField()
    Title = models.CharField(max_length=50)

#vote model is used for making sure nobody votes twice on the same poll, but does not save which selection they made
class Vote(models.Model):
    PollId = models.ForeignKey(Poll, on_delete=models.CASCADE)
    UserId = models.ForeignKey(User, on_delete=models.CASCADE)

class Message(models.Model):
    Title = models.CharField(max_length = 50)
    Body = models.CharField(max_length = 10000)
    DateSent = models.DateField()
    DateRead = models.DateField(null = True)
    SenderId = models.ForeignKey(User, null= True, on_delete=models.SET_NULL)#nullable and non cascade delete so that we can archive, send messages from system

# this model is used to make messages that are sent to multiple accounts
# a message has a MessageRecipientLink for every recipient of that message
class MessageRecipientLink(models.Model):
    MesageId = models.ForeignKey(Message, on_delete=models.CASCADE)
    UserId = models.ForeignKey(User, on_delete=models.CASCADE)
