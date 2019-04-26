from users.models import UserProfile

USERS = [
    {"username": "fky", "password": "password"},
    {"username": "xzc", "password": "password"},
    {"username": "xwy", "password": "password"},
    {"username": "jnr", "password": "password"},
    {"username": "lhh", "password": "password"},
]

for user in USERS:
    UserProfile(**user).save()
