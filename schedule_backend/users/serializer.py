from .models import UserProfile, Club, UserProfileClub, Membership
from rest_framework import serializers


class UserProfileSerializerUSER(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = UserProfile
        fields = ('url',
                  'username', 'realname', 'wechat_openID',
                  'email', 'mobile')


class ClubSerializerUSER(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Club
        fields = ('url',
                  'name', 'intro', 'avatar')
        read_only_fields = ('name', 'intro', 'avatar')


class MembershipSerializerUSER(serializers.HyperlinkedModelSerializer):
    club = ClubSerializerUSER()

    class Meta:
        model = Membership
        fields = (
            "url", "club",  "name",
            "is_admin",
            "date_created"
        )


##########################################
#
# #      USER ABOVE, ADMIN BELOW
#
##########################################

class UserProfileClubSerializerADMIN(serializers.HyperlinkedModelSerializer):
    # club = (read_only=True)
    club = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name="admin-club-detail"
    )

    membership = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name="admin-membership-detail"
    )

    class Meta:
        model = UserProfileClub
        fields = (
            'url', 'club', 'membership'
        )
        read_only_fields = ('club',)


class UserProfileSerializerCustom(serializers.HyperlinkedRelatedField):
    view_name = 'admin-user-detail'

    def get_queryset(self):
        return UserProfile.objects.all()


class MembershipSerializerCustom(serializers.HyperlinkedRelatedField):
    view_name = 'admin-membership-detail'

    def get_queryset(self):
        user = self.context['request'].user
        memberships = Membership.objects.filter(
            club__userProfileClub__userProfile=user, club__userProfileClub__membership__is_admin=True)
        return memberships


class UserProfileClubSerializerCustom(serializers.HyperlinkedModelSerializer):

    membership = serializers.HyperlinkedRelatedField(
        view_name="admin-membership-detail", read_only=True)

    class Meta:
        model = UserProfileClub
        fields = ('url', 'membership')
        # read_only_fields = ('intro',)


class UserProfileSerializerADMIN(serializers.HyperlinkedModelSerializer):
    """提供给管理者的信息"""
    url = serializers.HyperlinkedIdentityField(view_name="admin-user-detail")
    userProfileClub = UserProfileClubSerializerCustom(many=True)

    class Meta:
        model = UserProfile
        fields = ('url',
                  'username', 'realname',
                  'email', 'mobile', 'userProfileClub', 'timeline')
        read_only_fields = fields


class ClubSerializerADMIN(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="admin-club-detail")

    class Meta:
        model = Club
        fields = ('url',
                  'name', 'intro', 'avatar')


class ClubSerializerCustom(serializers.HyperlinkedRelatedField):
    view_name = 'admin-club-detail'

    def get_queryset(self):
        user = self.context['request'].user
        clubs = Club.objects.filter(
            userProfileClub__userProfile=user, userProfileClub__membership__is_admin=True)
        return clubs


class MembershipSerializerADMIN(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="admin-membership-detail")
    club = ClubSerializerCustom()

    class Meta:
        model = Membership
        fields = (
            "url", "club", "name",
            "is_admin",
            "date_created"
        )
        read_only_fields = ('date_created',)
