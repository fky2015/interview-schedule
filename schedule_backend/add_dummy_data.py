from users.models import UserProfile
user = UserProfile()
user.username = '1120202123'
user.set_password('password')
user.realname = '张三'
user.save()
