from django.db import models
from users.models import UserProfile, Membership
from users.models import Club

# TODO if it's reasonable to use CASCADE on every foreignkey

# 记录一次面试的信息
# 一次面试是指有一定意义的一场面试，比如春招、秋招等
# 面试由一系列面试表组成


class Interview(models.Model):
    club = models.ForeignKey(
        Club, related_name="interview", on_delete=models.CASCADE)
    title = models.CharField(verbose_name="Interview Title", max_length=100)
    description = models.TextField(max_length=600)
    edit_finish = models.BooleanField(default=False)  # 是否处于可编辑状态
    is_public = models.BooleanField(
        verbose_name="if it's public", default=False)
    out_state = models.FileField(Membership)  # 面试成功后要到达的状态

    class Meta:
        order_with_respect_to = 'club'

    def __str__(self):
        return f'{self.club} - {self.title}'

# 只有处于in_state 状态中的成员才能选择该面试，通过者
# 会移动到 out_state 状态


class InState(models.Model):
    interview = models.ForeignKey(
        Interview, related_name="in_state", on_delete=models.CASCADE
    )
    membership = models.ForeignKey(
        Membership, on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ('interview', 'membership')

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
    passed = models.BooleanField(
        verbose_name="pass the interview", default=False)

    class Meta:
        unique_together = ('interviewTimeline', 'user')  # 多列联合唯一性约束
        # 一个人在一个面试场最多只能报名一次
