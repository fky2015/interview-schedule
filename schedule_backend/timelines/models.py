from django.db import models
from users.models import UserProfile
from users.models import Club


# Create your models here.

# 记录一次面试的信息
# 一次面试是指有一定意义的一场面试，比如春招、秋招等
# 面试由一系列面试表组成
class Interview(models.Model):
    club = models.ForeignKey(
        Club, related_name="interview", on_delete=models.CASCADE)
    title = models.CharField(verbose_name="Interview Title", max_length=100)
    description = models.TextField(max_length=600)

    class Meta:
        order_with_respect_to = 'club'

    def __str__(self):
        # TODO format string ?
        return str(self.club) + ' - ' + self.title

# 记录场面试的面试表
# 面试表是指一次面试中某一个有具体地点和时间长度的面试


class InterviewTimeline(models.Model):
    interview = models.ForeignKey(
        Interview, related_name="InterviewTimeline", on_delete=models.CASCADE)
    location = models.TextField(max_length=100)
    title = models.CharField(max_length=100)

    class Meta:
        order_with_respect_to = 'interview'

    def __str__(self):
        return str(self.interview) + '-' + self.location

# 时间片是指对于一个人来说的,
# 时间片是面试中最小的组成单元


class Timeline(models.Model):
    interviewTimeline = models.ForeignKey(
        InterviewTimeline, on_delete=models.CASCADE)
    user = models.ForeignKey(
        UserProfile, on_delete=models.SET_NULL, null=True, blank=True)
    startTime = models.DateTimeField()
    duration = models.IntegerField(verbose_name="duration( /minutes)")
