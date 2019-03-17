from django.shortcuts import render
from .models import InterviewTimeline, Interview, Timeline,\
    InState
from .serializer import InterviewSerializer, \
    InterviewTimelineSerializer, TimelineSerializer, \
    InStateSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action


class InterviewViewSet(viewsets.ModelViewSet):
    queryset = Interview.objects.all()
    serializer_class = InterviewSerializer

# for User,
# 用户只能看见可以选的
class InterviewViewSet_User(viewsets.ModelViewSet):
    queryset = Interview.objects.all()
    serializer_class = InterviewSerializer


class InterviewTimelineViewSet(viewsets.ModelViewSet):
    queryset = InterviewTimeline.objects.all()
    serializer_class = InterviewTimelineSerializer


class TimelineViewSet(viewsets.ModelViewSet):
    queryset = Timeline.objects.all()
    serializer_class = TimelineSerializer

    def list(self, request):
        queryset = Timeline.objects.filter(user=request.user)
        serializer = TimelineSerializer(
            queryset, many=True, context={'request': request})
        return Response(serializer.data)

    # TODO
    # 普通用户只对它的user字段有操作能力
    # admin用户才能修改其他部分


class InStateViewSet(viewsets.ModelViewSet):
    queryset = InState.objects.all()
    serializer_class = InStateSerializer
