from .models import UserProfile, Club, UserProfileClub
from rest_framework import serializers


class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('url',
                  'username', 'realname', 'email', 'mobile', 'groups')


class ClubSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Club
        fields = ('url',
                  'name', 'intro', 'avatar')


class UserProfileClubSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = UserProfileClub
        fields = (
            'url', 'userProfile', 'club', 'membership'
        )
