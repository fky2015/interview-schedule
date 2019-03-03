from django.db import models
from users.models import UserProfile
from users.models import Club


# Create your models here.


class Interview(models.Model):
    club = models.ForeignKey(
        Club, related_name="interview", on_delete=models.CASCADE)
    title = models.CharField(verbose_name="Interview Title", max_length=100)

    class Meta:
        order_with_respect_to = 'club'


class InterviewTimeline(models.Model):
    interview = models.ForeignKey(
        Interview, related_name="InterviewTimeline", on_delete=models.CASCADE)
    location = models.TextField(max_length=100)

    class Meta:
        order_with_respect_to = 'interview'


class Timeline(models.Model):
    interviewTimeline = models.ForeignKey(
        InterviewTimeline, on_delete=models.CASCADE)
    user = models.ForeignKey(
        UserProfile, on_delete=models.SET_NULL, null=True, blank=True)
    startTime = models.DateTimeField()
    duration = models.IntegerField(verbose_name="duration( /minutes)")
