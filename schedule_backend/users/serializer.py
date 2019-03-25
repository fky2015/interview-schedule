from .models import UserProfile, Club, UserProfileClub, Membership
from rest_framework import serializers


class UserProfileSerializerUSER(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = UserProfile
        fields = ('url',
                  'username', 'realname',
                  'email', 'mobile', 'groups')


class UserProfileSerializerUSER(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('url',
                  'username', 'realname',
                  'email', 'mobile', 'groups')


class ClubSerializerPUBLIC(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Club
        fields = ('url',
                  'name', 'intro', 'avatar')

class ClubSerializerADMIN(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Club
        fields = ('url',
                  'name', 'intro', 'avatar')

class UserProfileClubSerializerUSER(serializers.HyperlinkedModelSerializer):

    # userProfile = UserProfileSerializer()
    # club = ClubSerializer()

    class Meta:
        model = UserProfileClub
        fields = (
            'url', 'userProfile', 'club', 'membership'
        )


class MembershipSerializerUSER(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Membership
        fields = (
            "url", "club",  "name",
            "can_edit", "can_schedule", "can_export",
            "date_created"
        )
