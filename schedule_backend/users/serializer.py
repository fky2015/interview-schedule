from .models import UserProfile, Club, UserProfileClub, Membership
from rest_framework import serializers


class UserProfileSerializerUSER(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = UserProfile
        fields = ('url',
                  'username', 'realname',
                  'email', 'mobile')


class UserProfileSerializerPUBLIC(serializers.HyperlinkedModelSerializer):
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
    club = ClubSerializerPUBLIC(read_only=True)
    # club = serializers.HyperlinkedRelatedField(
    #     read_only=True,
    #     view_name="club-detail"
    # )

    class Meta:
        model = UserProfileClub
        fields = (
            'url', 'club', 'membership'
        )


class MembershipSerializerUSER(serializers.HyperlinkedModelSerializer):
    club = ClubSerializerPUBLIC()

    class Meta:
        model = Membership
        fields = (
            "url", "club",  "name",
            "can_edit", "can_schedule", "can_export",
            "date_created"
        )
