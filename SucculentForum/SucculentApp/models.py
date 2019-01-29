from django.db import models

# Create your models here.

class Topic(models.Model):
    Title = models.CharField(max_length=50)
    DateUpdated = models.DateField()
    ThreadCount = models.IntegerField()

class Thread(models.Model):
    Title = models.CharField(max_length=50)
    DateUpdated = models.DateField()
    Body = models.CharField(max_length=50)
    UserId = models.ForeignKey(User, on_delete=models.CASCADE)
    ViewCount = models.IntegerField()
    TopicId = models.ForeignKey(Topic, on_delete=models.CASCADE)
    DateStarted = models.DateField()
    PostCount = models.IntegerField()

