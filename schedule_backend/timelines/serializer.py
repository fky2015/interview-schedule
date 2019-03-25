from .models import Interview, InterviewTimeline, Timeline, InState
from rest_framework import serializers


class InterviewSerializerPUBLIC(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Interview
        fields = ('url', 'club', 'title')

class InterviewSerializerADMIN(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Interview
        fields = ('url', 'club', 'title')


class InterviewTimelineSerializerPUBLIC(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InterviewTimeline
        fields = ('url', 'interview', 'location')

# 仅仅被用户使用的话，不需要user这个field
class InterviewTimelineSerializerADMIN(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InterviewTimeline
        fields = ('url', 'interview', 'location')



class TimelineSerializerUSER(serializers.HyperlinkedModelSerializer):

    # interviewTimeline = InterviewTimelineSerializer()

    class Meta:
        model = Timeline
        fields = ('url', 'interviewTimeline', 'user',
                  'startTime', 'duration', 'timeID')

class TimelineSerializerPUBLIC(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Timeline
        fields = ('url', 'interviewTimeline', 'user',
                  'startTime', 'duration', 'timeID')

class TimelineSerializerADMIN(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Timeline
        fields = ('url', 'interviewTimeline', 'user',
                  'startTime', 'duration', 'timeID')




class InStateSerializerADMIN(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = InState
        fields = ('url', 'interview', 'membership')
