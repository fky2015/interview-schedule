# Membership
    
-  关系表，储存用户与社团关系
- uid已略去

| 字段        | 类型     | 空   | 默认     | 注释     |
| :----       | :------- | :--- | -- -     | ------   |
| date_joined | Date     | 否   | 创建时间 |          |
| level       | char(12) | 否   |          | 关系级别 |

- 备注：无

```Python
class Membership(models.Model):
    MEMBERSHIP_LEVEL = (
        ('interviewer', '面试者'),
        ('interviewee', '被面试者')
    )  # TODO: 加入更合理的选项
    userProfile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    date_joined = models.DateField()
    level = models.CharField(max_length=12, choices=MEMBERSHIP_LEVEL)
```