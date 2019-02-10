from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

# 采用继承AbstractUser 的方式，而不是使用 OneToOneFiled


class UserProfile(AbstractUser):
    GENDER_CHOICE = (
        ('male', '男'),
        ('female', '女'),
        ('secret', '保密'),

    )
    intro = models.TextField(verbose_name="self introduction", blank=True)
    real_name = models.CharField(verbose_name="real name", max_length=50)
    gender = models.CharField(
        verbose_name="性别", choices=GENDER_CHOICE, default='secret', max_length=8)
    studentID = models.CharField(verbose_name="student id", max_length=10, help_text='学号，一般来说是十位（BIT）')
    wechat_openID = models.CharField(max_length=100, blank=True)
    mobile = models.CharField(max_length=11)
    avatar = models.ImageField(upload_to='image', blank=True,
                               null=True, default="image/default.png", max_length=100)

    class Meta:
        verbose_name = "user information"
        verbose_name_plural = verbose_name
        ordering = ['studentID']

    def __str__(self):
        return self.username


class Club(models.Model):
    userProfile = models.ManyToManyField(UserProfile)
    name = models.CharField(verbose_name="社团名称", max_length=100)
    intro = models.TextField(verbose_name="self_introduction", blank=True)
    avatar = models.ImageField(
        upload_to='image', blank=True, null=True, max_length=100)

    def __str__(self):
        return self.name


class Membership(models.Model):
    MEMBERSHIP_LEVEL = (
        ('interviewer', '面试者'),
        ('interviewee', '被面试者')
    )  # TODO: 加入更合理的选项
    userProfile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    date_joined = models.DateField()
    level = models.CharField(max_length=12, choices=MEMBERSHIP_LEVEL)

    class Meta():
        verbose_name = 'membership'
        verbose_name_plural = verbose_name
