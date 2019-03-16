from .models import UserProfile, Club, UserProfileClub, Membership
from rest_framework import serializers


class CurrentUserProfileSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = UserProfile
        fields = ('url',
                  'username', 'realname',
                  'email', 'mobile', 'groups')


class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('url',
                  'username', 'realname',
                  'email', 'mobile', 'groups')


class ClubSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Club
        fields = ('url',
                  'name', 'intro', 'avatar')


class UserProfileClubSerializer(serializers.HyperlinkedModelSerializer):

    # userProfile = UserProfileSerializer()
    # club = ClubSerializer()

    class Meta:
        model = UserProfileClub
        fields = (
            'url', 'userProfile', 'club', 'membership'
        )


class MembershipSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Membership
        fields = (
            "url", "club",  "name",
            "can_edit", "can_schedule", "can_export",
            "date_created"
        )
