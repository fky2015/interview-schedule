from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import validate_mobile
# Create your models here.

# 用户


class UserProfile(AbstractUser):
    """记录用户信息"""
    GENDER_CHOICE = (
        ('male', '男'),
        ('female', '女'),
        ('secret', '保密'),

    )
    # 学号是username
    intro = models.TextField(
        verbose_name="自我介绍", blank=True, help_text="用简短的话语介绍自己，可选。")
    realname = models.CharField(verbose_name="真实姓名", max_length=50)
    gender = models.CharField(
        verbose_name="性别", choices=GENDER_CHOICE, default='secret', max_length=8)
    wechat_openID = models.CharField(
        verbose_name="wechat openID", help_text="用于微信小程序登录", max_length=100, blank=True)
    mobile = models.CharField(
        verbose_name="手机号", help_text="帮助社团联系到你", max_length=11, blank=True, validators=[validate_mobile])
    # TODO: 了解 Image 细节
    avatar = models.ImageField(verbose_name="头像", upload_to='image/%Y-%m-%d', blank=True,
                               null=True, default="image/default.png", max_length=None)

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return self.username


# 社团
class Club(models.Model):
    """社团"""
    VERIFY_CHOICE = (
        ('unverified', '验证中'),
        ('failed', '未通过'),
        ('pass', '通过'),
    )

    # userProfile = models.ManyToManyField(UserProfile)
    name = models.CharField(verbose_name="社团名称", max_length=100, unique=True)
    intro = models.TextField(verbose_name="社团简介", blank=True)
    avatar = models.ImageField(
        upload_to='image', blank=True, null=True, max_length=100)
    verified = models.CharField(
        verbose_name="验证状态", choices=VERIFY_CHOICE, default='unverified', max_length=10)  # TODO

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
    membership = models.ForeignKey("Membership", related_name="userProfileClub", on_delete=models.SET_NULL, blank=True,
                                   null=True,)  # 当存在这条，而membership为NULL和不存在这条有什么区别呢

    class Meta:
        unique_together = ('userProfile', 'club')  # 多列联合唯一性约束

    def __str__(self):
        return '['+str(self.userProfile) + ']-[' + str(self.club)+']'


class Membership(models.Model):
    # 外键： Club interview
    club = models.ForeignKey(
        Club, related_name="membership", on_delete=models.CASCADE)  # 一个 社团有多个角色
    # 名称唯一
    name = models.CharField(verbose_name="关系名称", max_length=50)
    is_admin = models.BooleanField(verbose_name="是否为社团管理者", default=False)
    # can_schedule = models.BooleanField(verbose_name="是否可以安排面试", default=False)
    # can_export = models.BooleanField(verbose_name="是否可以导出信息", default=False)
    date_created = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'membership'
        verbose_name_plural = verbose_name
        unique_together = ('club', 'name')  # 多列联合唯一性约束

    def __str__(self):
        return f"{self.club} - {self.name}"
