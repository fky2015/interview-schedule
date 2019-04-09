from .models import Interview, InterviewTimeline, Timeline, InState
from users.serializer import MembershipSerializerUSER
from rest_framework import serializers


class InterviewSerializerUSER(serializers.HyperlinkedModelSerializer):
    # out_state = MembershipSerializerUSER(read_only=True)

    class Meta:
        model = Interview
        fields = ('url', 'club', 'title', 'description',
                  'edit_finish', 'is_public', 'out_state')


class InterviewTimelineSerializerUSER(serializers.HyperlinkedModelSerializer):

    # interview = InterviewSerializerPUBLIC()

    class Meta:
        model = InterviewTimeline
        fields = ('url', 'interview', 'location')

# 仅仅被用户使用的话，不需要user这个field


class TimelineSerializerUSER(serializers.HyperlinkedModelSerializer):
    """用于user查看自己的timeline"""

    interviewTimeline = InterviewTimelineSerializerUSER(read_only=True)
    # TODO may be 换成 USER的？

    class Meta:
        model = Timeline
        fields = ('url', 'interviewTimeline', 'user',
                  'startTime', 'duration', 'timeID')


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


class InterviewSerializerADMIN(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Interview
        fields = ('url', 'club', 'title')


class InterviewTimelineSerializerADMIN(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InterviewTimeline
        fields = ('url', 'interview', 'location')


class TimelineSerializerADMIN(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Timeline
        fields = ('url', 'interviewTimeline', 'user',
                  'startTime', 'duration', 'timeID')


class InStateSerializerADMIN(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = InState
        fields = ('url', 'interview', 'membership')
