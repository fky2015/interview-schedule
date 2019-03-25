from django.shortcuts import render
from .models import InterviewTimeline, Interview, Timeline,\
    InState
from .serializer import InterviewSerializerPUBLIC, \
    InterviewTimelineSerializerPUBLIC, TimelineSerializerUSER, \
    InStateSerializerADMIN, TimelineSerializerPUBLIC, \
        InterviewSerializerADMIN, InterviewTimelineSerializerADMIN, \
            TimelineSerializerADMIN
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action


class InterviewViewSetPUBLIC(viewsets.ModelViewSet):
    queryset = Interview.objects.all()
    serializer_class = InterviewSerializerPUBLIC

# for User,
# 用户只能看见可以选的
class InterviewViewSetUSER(viewsets.ModelViewSet):
    queryset = Interview.objects.all()
    serializer_class = InterviewSerializerPUBLIC

class InterviewViewSetADMIN(viewsets.ModelViewSet):
    queryset = Interview.objects.all()
    serializer_class = InterviewSerializerADMIN


class InterviewTimelineViewSetPUBLIC(viewsets.ModelViewSet):
    queryset = InterviewTimeline.objects.all()
    serializer_class = InterviewTimelineSerializerPUBLIC


class TimelineViewSetUSER(viewsets.ModelViewSet):
    queryset = Timeline.objects.all()
    serializer_class = TimelineSerializerUSER

    def list(self, request):
        queryset = Timeline.objects.filter(user=request.user)
        serializer = TimelineSerializerUSER(
            queryset, many=True, context={'request': request})
        return Response(serializer.data)

    # TODO
    # 普通用户只对它的user字段有操作能力
    # admin用户才能修改其他部分

class InterviewTimelineViewSetADMIN(viewsets.ModelViewSet):
    queryset = InterviewTimeline.objects.all()
    serializer_class = InterviewTimelineSerializerADMIN

class TimelineViewSetPUBLIC(viewsets.ModelViewSet):
    queryset = Timeline.objects.all()
    serializer_class = TimelineSerializerPUBLIC

class TimelineViewSetADMIN(viewsets.ModelViewSet):
    queryset = Timeline.objects.all()
    serializer_class = TimelineSerializerADMIN




class InStateViewSetADMIN(viewsets.ModelViewSet):
    queryset = InState.objects.all()
    serializer_class = InStateSerializerADMIN
