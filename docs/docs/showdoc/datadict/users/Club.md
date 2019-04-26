# Club
    
-  社团表，储存社团信息
- uid 略去

| 字段   | 类型      | 空   | 默认        | 注释     |     |
| :----- | :-------- | :--- | ----------- | -------- | --- |
| name   | char(100) | 否   |             | 社团名称 |     |
| intro  | text      | 是   |             | 社团简介 |     |
| avatar | int(11)   | 是   | default.jpg | 图片     |     |

- 备注：无


Club代码
```Python
class Club(models.Model):
    userProfile = models.ManyToManyField(UserProfile)
    name = models.CharField(verbose_name="社团名称", max_length=100)
    intro = models.TextField(verbose_name="self_introduction", blank=True)
    avatar = models.ImageField(
        upload_to='image', blank=True, null=True, max_length=100)

    def __str__(self):
        return self.name
```