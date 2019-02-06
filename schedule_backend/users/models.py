from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField("self_introduction", blank=True)
    studentID = models.TextField(verbose_name="student id", max_length=10)
    wechat_openID = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=12)
    email = models.EmailField()
    avatar = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.user


class Club(models.Model):
    user = models.ManyToManyField(User)
    name = models.CharField(verbose_name="社团名称", max_length=100)
    intro = models.TextField("self_introduction", blank=True)
    avatar = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name


class Membership(models.Model):
    MEMBERSHIP_LEVEL = (
        ('S', 'Small'),
    )# TODO: 加入更合理的选项
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    date_joined = models.DateField()
    level = models.CharField(max_length=5, choices=MEMBERSHIP_LEVEL)
