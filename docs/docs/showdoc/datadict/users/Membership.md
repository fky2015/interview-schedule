# Membership
    
-  关系表，储存用户与社团关系
- uid已略去

| 字段         | 类型     | 空   | 默认 | 注释     |
| :----------- | :------- | :--- | ---- | -------- |
| club         | Date     | 否   |      |  club        |
| name         | char(12) | 否   |      | 关系的名称|
| can_edit     | bool     | 否   | 否   |     can edit?     |
| can_schedule | bool     | 否   | 否   |    是否安排面试      |
| can_export   | bool     |      | 否   |   是否可以导出信息       |
| date_created | datetime |      | now  |    创建时间      |

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