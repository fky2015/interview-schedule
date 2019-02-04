from django.db import models
from django.contrib.auth.models import User
from users.models import Club
# Create your models here.


class Interview(models.Model):
    name = models.CharField(max_length=100)


class InterviewTimelines(models.Model):
    interview = models.ForeignKey(Interview, on_delete=models.CASCADE)
    location = models.TextField(max_length=100)


class timeline(models.Model):
    interviewTimelines = models.ForeignKey(
        InterviewTimelines, on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    startTime = models.DateTimeField()
    duration = models.IntegerField(verbose_name="duration( /minutes)")
