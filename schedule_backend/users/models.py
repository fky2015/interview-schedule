from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

# 用户


class UserProfile(AbstractUser):
    GENDER_CHOICE = (
        ('male', '男'),
        ('female', '女'),
        ('secret', '保密'),

    )
    # 学号是username
    intro = models.TextField(verbose_name="self introduction", blank=True)
    realname = models.CharField(verbose_name="real name", max_length=50)
    gender = models.CharField(
        verbose_name="性别", choices=GENDER_CHOICE, default='secret', max_length=8)
    wechat_openID = models.CharField(max_length=100, blank=True)
    mobile = models.CharField(max_length=11)
    avatar = models.ImageField(upload_to='image', blank=True,
                               null=True, default="image/default.png", max_length=100)

    class Meta:
        verbose_name = "user information"
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return self.username


# 社团
class Club(models.Model):
    # userProfile = models.ManyToManyField(UserProfile)
    name = models.CharField(verbose_name="社团名称", max_length=100)
    intro = models.TextField(verbose_name="self_introduction", blank=True)
    avatar = models.ImageField(
        upload_to='image', blank=True, null=True, max_length=100)

    class Meta():
        verbose_name = 'club'
        verbose_name_plural = "clubs"

    def __str__(self):
        return self.name


# Many to Many 的表，存放Membership
class UserProfileClub(models.Model):
    userProfile = models.ForeignKey(
        UserProfile, related_name="userProfileClub", on_delete=models.CASCADE)
    club = models.ForeignKey(
        Club, related_name="userProfileClub", on_delete=models.CASCADE)
    membership = models.ForeignKey("Membership", on_delete=models.SET_NULL, blank=True,
                                   null=True,)  # 当存在这条，而membership为NULL和不存在这条有什么区别呢

    class Meta:
        unique_together = ('userProfile', 'club')  # 多列联合唯一性约束

    def __str__(self):
        return '['+str(self.userProfile) + ']-[' + str(self.club)+']'


class Membership(models.Model):
    # 外键： Club interview
    club = models.ForeignKey(
        Club, related_name="membership", on_delete=models.CASCADE)  # 一个 社团有多个角色
    # interview = models.ManyToManyField(
    #     'timelines.Interview', related_name="membership", blank=True)
    name = models.CharField(verbose_name="关系名称", max_length=50)
    can_edit = models.BooleanField(verbose_name="是否可以修改社团信息", default=False)
    can_schedule = models.BooleanField(verbose_name="是否可以安排面试")
    can_export = models.BooleanField(verbose_name="是否可以导出信息")
    date_created = models.DateField(auto_now=True)

    class Meta():
        verbose_name = 'membership'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.club} - {self.name}"
