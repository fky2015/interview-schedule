from django.db import models
from users.models import UserProfile, Membership
from users.models import Club


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
    out_state = models.ForeignKey(
        Membership, on_delete=models.PROTECT, blank=True, null=True)  # 面试成功后要到达的状态

    class Meta:
        order_with_respect_to = 'club'

    def __str__(self):
        return f'{self.club} - {self.title}'


class InState(models.Model):
    """只有处于in_state 状态中的成员才能选择该面试，通过者
    会移动到 out_state 状态"""
    interview = models.ForeignKey(
        Interview, related_name="in_state", on_delete=models.CASCADE
    )
    membership = models.ForeignKey(
        Membership, related_name="in_state", on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ('interview', 'membership')

    def __str__(self):
        return f"{self.interview}-{self.membership}"


class InterviewTimeline(models.Model):
    """记录场面试的面试表
    面试表是指一次面试中某一个有具体地点和时间长度的面试"""

    interview = models.ForeignKey(
        Interview, related_name="interviewTimeline", on_delete=models.CASCADE)
    location = models.CharField(verbose_name="面试地点", max_length=100)
    remarks = models.TextField(verbose_name="备注", max_length=100)
    date = models.DateField(verbose_name="日期")
    startTime = models.TimeField(verbose_name='开始时间', default="18:30")
    endTime = models.TimeField(verbose_name='结束时间', default="21:00")

    class Meta:
        # order_with_respect_to = 'interview'
        ordering = ['date', 'startTime']

    def __str__(self):
        return f'{self.interview}-{self.location}'


# 时间片是指对于一个人来说的,
# 时间片是面试中最小的组成单元


class Timeline(models.Model):
    interviewTimeline = models.ForeignKey(InterviewTimeline,
                                          related_name="timeline",
                                          on_delete=models.CASCADE)
    user = models.ForeignKey(
        UserProfile, related_name='timeline', on_delete=models.SET_NULL, null=True, blank=True)
    timeID = models.IntegerField(
        default=0, verbose_name="时间ID", help_text="用于帮助区分统一时间段的不同时间片")
    startTime = models.TimeField(verbose_name="开始时间")
    duration = models.IntegerField(verbose_name="duration( /minutes)")
    intro = models.TextField('自我介绍', blank=True, null=True)
    comment = models.TextField(
        verbose_name="comment", max_length=200, default="")
    passed = models.BooleanField(
        verbose_name="pass the interview", default=False)

    class Meta:
        ordering = ('startTime','timeID')
        unique_together = ('interviewTimeline', 'user')  # 多列联合唯一性约束
        # 一个人在一个面试场最多只能报名一次

    def __str__(self):
        return f"{self.interviewTimeline}-{self.user}-{self.timeID}"
