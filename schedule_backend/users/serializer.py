from .models import UserProfile, Club
from rest_framework import serializers


class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('url',
                  'username', 'email', 'groups')


class ClubSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Club
        fields = ('url',
                  'name', 'intro', 'avatar')
