# UserProfile
    
-  用户表，储存用户信息 继承原有的`AbstractUser`
- username, first_name, last_name, email, is_staff, is_active, data_joined 属于`AbstractUser`，在此略去，详见源码或者数据库。

| 字段          | 类型      | 空   | 默认        | 注释                     |
| :----         | :-------  | :--- | -- -        | ------                   |
| intro         | text      | 是   |             | 自我介绍                 |
| real_name     | char(50)  | 否   |             | 真实姓名                 |
| gender        | char(8)   | 否   | secret      | 性别，实际上是一个choice |
| studentID     | char(10)  | 否   |             | 学号                     |
| wechat_openID | char(100) | 否   | 0           | 注册时间                 |
| mobile        | char(11)  | 是   |             | 手机号                   |
| avatar        | char(100) | 是   | default.png | 存储头像路径             |

- 备注：为了保证CAS插件可用，可能还要修改扩展策略（乖乖使用User+Profile) // TODO: 待测试



## `AbstractUser` 代码

```python
class AbstractUser(AbstractBaseUser, PermissionsMixin):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.

    Username and password are required. Other fields are optional.
    """
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    email = models.EmailField(_('email address'), blank=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
```