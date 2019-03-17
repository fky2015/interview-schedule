from .models import Interview, InterviewTimeline, Timeline, InState
from rest_framework import serializers


class InterviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Interview
        fields = ('url', 'club', 'title')


class InterviewTimelineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InterviewTimeline
        fields = ('url', 'interview', 'location')

# 仅仅被用户使用的话，不需要user这个field


class TimelineSerializer(serializers.HyperlinkedModelSerializer):

    interviewTimeline = InterviewTimelineSerializer()

    class Meta:
        model = Timeline
        fields = ('url', 'interviewTimeline', 'user',
                  'startTime', 'duration')


class InStateSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = InState
        fields = ('url', 'interview', 'membership')
