from .models import Interview, InterviewTimeline, Timeline
from rest_framework import serializers


class InterviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Interview
        fields = ('url', 'club', 'title')


class InterviewTimelineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InterviewTimeline
        fields = ('url', 'interview', 'location')


class TimelineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Timeline
        fields = ('url', 'interviewTimeline', 'startTime', 'duration')
