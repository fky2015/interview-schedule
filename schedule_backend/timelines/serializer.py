from rest_framework import serializers

from users.serializer import (ClubSerializerCustom, ClubSerializerUSER, MembershipSerializerCustom,
                              MembershipSerializerUSER,
                              UserProfileSerializerCustom, UserProfileSerializerADMIN, UserProfileSerializerUSER)

from .models import InState, Interview, InterviewTimeline, Timeline


class TimelineSerializerUserCustom(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Timeline
        fields = ('url', 'startTime', 'duration')


class InterviewTimelineSerializerUserCustom(serializers.HyperlinkedModelSerializer):
    # timeline = TimelineSerializerUserCustom(read_only=True, many=True)

    class Meta:
        model = InterviewTimeline
        fields = ('url', 'location', 'date',
                  'startTime', 'endTime')


class InterviewSerializerUSER(serializers.HyperlinkedModelSerializer):
    out_state = MembershipSerializerUSER(read_only=True)
    # interviewTimeline = serializers.SlugRelatedField(
    # read_only=True, slug_field='location', many=True)
    interviewTimeline = InterviewTimelineSerializerUserCustom(
        many=True, read_only=True)

    class Meta:
        model = Interview
        fields = ('url', 'club', 'title', 'description',
                  'edit_finish', 'out_state', 'interviewTimeline')
        # read_only_fields = (,)

class InterviewSerializerUSERUP(serializers.HyperlinkedModelSerializer):
    club = ClubSerializerUSER(read_only=True)
    class Meta:
        model = Interview
        fields = ('url', 'club', 'title', )

class InterviewTimelineSerializerUSER(serializers.HyperlinkedModelSerializer):

    interview = InterviewSerializerUSERUP(read_only=True)

    class Meta:
        model = InterviewTimeline
        fields = ('url', 'interview', 'location')

# 仅仅被用户使用的话，不需要user这个field


class TimelineSerializerUSER(serializers.HyperlinkedModelSerializer):
    """用于user查看自己的timeline"""

    interviewTimeline = InterviewTimelineSerializerUSER(read_only=True)
    # club
    # TODO may be 换成 USER的？

    class Meta:
        model = Timeline
        fields = ('url', 'interviewTimeline', 'user',
                  'startTime', 'duration', 'timeID',)


class TimelineSerializerPUBLIC(serializers.HyperlinkedModelSerializer):
    """用于public api"""
    class Meta:
        model = Timeline
        fields = ('url', 'interviewTimeline', 'user',
                  'startTime', 'duration', 'timeID')


class InStateSerializerUSER(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = InState
        fields = ('url', 'interview', 'membership')

##########################################
#
# #      USER ABOVE, ADMIN BELOW
#
##########################################


class InterviewSerializerCustom(serializers.HyperlinkedRelatedField):
    view_name = 'admin-interview-detail'

    def get_queryset(self):
        user = self.context['request'].user
        print(user)

        interviews = Interview.objects.filter(
            club__userProfileClub__userProfile=user, club__userProfileClub__membership__is_admin=True)
        return interviews


class InterviewTimelineSerializerADMIN(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="admin-interviewtimeline-detail")
    interview = InterviewSerializerCustom()

    class Meta:
        model = InterviewTimeline
        fields = ('url', 'pk', 'interview', 'location', 'date', 'remarks')


class InterviewSerializerADMIN(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="admin-interview-detail", read_only=True)
    interviewTimeline = InterviewTimelineSerializerADMIN(
        many=True, read_only=True)
    club = ClubSerializerCustom()
    out_state = MembershipSerializerCustom()

    class Meta:
        model = Interview
        fields = ('url',  'pk', 'club', 'title', 'description', 'edit_finish', 'is_public',
                  'interviewTimeline', 'out_state')
        read_only_fields = ('url', 'pk', 'interviewTimeline',)


class InterviewTimelineSerializerCustom(serializers.HyperlinkedRelatedField):
    view_name = 'admin-interviewtimeline-detail'

    def get_queryset(self):
        user = self.context['request'].user
        print(user)
        interviewTimelines = InterviewTimeline.objects.filter(
            interview__club__userProfileClub__userProfile=user, interview__club__userProfileClub__membership__is_admin=True)
        return interviewTimelines


class TimelineSerializerADMIN(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="admin-timeline-detail")
    user = UserProfileSerializerCustom(allow_null=True)
    interviewTimeline = InterviewTimelineSerializerCustom()

    class Meta:
        model = Timeline
        fields = ('url', 'interviewTimeline', 'user',
                  'startTime', 'duration', 'passed', 'comment', 'timeID')


class TimelineSerializerADMINApplicant(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="admin-timeline-detail")
    user = UserProfileSerializerUSER(allow_null=True)
    interviewTimeline = InterviewTimelineSerializerADMIN()

    class Meta:
        model = Timeline
        fields = ('url', 'interviewTimeline', 'user',
                  'startTime', 'duration', 'passed', 'comment', 'timeID')


class InStateSerializerADMIN(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="admin-instate-detail")
    interview = InterviewSerializerCustom()
    membership = MembershipSerializerCustom()

    class Meta:
        model = InState
        fields = ('url', 'interview', 'membership')
