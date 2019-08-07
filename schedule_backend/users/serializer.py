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


class UserProfileClubSerializerUSER(serializers.HyperlinkedModelSerializer):
    club = ClubSerializerUSER(read_only=True)
    # club = serializers.HyperlinkedRelatedField(
    #     read_only=True,
    #     view_name="club-detail"
    # )

    class Meta:
        model = UserProfileClub
        fields = (
            'url', 'club'
        )


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

class UserProfileSerializerADMIN(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('url',
                  'username', 'realname',
                  'email', 'mobile', 'groups')


class ClubSerializerADMIN(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Club
        fields = ('url',
                  'name', 'intro','avatar')


class MembershipSerializerADMIN(serializers.HyperlinkedModelSerializer):
    club = ClubSerializerADMIN()

    class Meta:
        model = Membership
        fields = (
            "url", "club",  "name",
            "is_admin",
            "date_created"
        )
