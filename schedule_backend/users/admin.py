from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile, Club, UserProfileClub, Membership


# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    fields = (
        'username', 'mobile', 'realname',
        'is_staff', 'is_active',
        'email', 'first_name', 'last_name',
        'intro', 'gender',
        'studentNumber'
    )


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Club)
admin.site.register(UserProfileClub)
admin.site.register(Membership)
