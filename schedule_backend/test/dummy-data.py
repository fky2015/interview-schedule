from users.models import UserProfile

users = [('fky', 'password'), ('xzc', 'xzc'), ('xwy', 'xwy')]

for i, j in users:
    UserProfile.objects.get_or_create(username=i, password=j)
