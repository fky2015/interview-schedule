from django.db import models

# Create your models here.

class Feed(models.Model):
    """feed（动态），将来可能迁移至redis"""
    CATEGORY_CHOICE = (
        ('type1',"type1"),
        ('type2',"type2"),
        ('type3',"type3"),
    )

    title = models.CharField(max_length=50)
    link = models.CharField(max_length=200,verbose_name='related link')
    content = models.TextField()
    category = models.CharField(choices=CATEGORY_CHOICE,max_length=20) # 新闻属性
    createTime = models.DateTimeField(verbose_name="created time",auto_now=True)