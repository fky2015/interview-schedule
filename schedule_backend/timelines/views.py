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
from rest_framework.permissions import AllowAny, IsAdminUser


class InterviewViewSet(viewsets.ModelViewSet):
    """面试"""
    queryset = Interview.objects.all()
    serializer_class = InterviewSerializerPUBLIC

    def get_permissions(self):
        if self.action in ['list', 'retrieve', 'interviewTimeline']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

    @action(detail=True, methods=['GET'])
    def interviewTimeline(self, request, pk=None):
        """返回该面试下的所有面试表"""
        interview = self.get_object()
        queryset = InterviewTimeline.objects.filter(interview=interview)

        serializer = InterviewTimelineSerializerPUBLIC(
            queryset, many=True, context={'request': request}
        )
        return Response(serializer.data)


# class InterviewViewSetUSER(viewsets.ModelViewSet):
#     queryset = Interview.objects.all()
#     serializer_class = InterviewSerializerPUBLIC


# class InterviewViewSetADMIN(viewsets.ModelViewSet):
#     queryset = Interview.objects.all()
    # serializer_class = InterviewSerializerADMIN


class InterviewTimelineViewSet(viewsets.ModelViewSet):
    queryset = InterviewTimeline.objects.all()
    serializer_class = InterviewTimelineSerializerPUBLIC

    def get_permissions(self):
        if self.action in ['list', 'retrieve', 'timeline']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

    @action(detail=True, methods=['GET'])
    def timeline(self, request, pk=None):
        obj = self.get_object()
        queryset = Timeline.objects.filter(interviewTimeline=obj)
        serializer = TimelineSerializerUSER(
            queryset, many=True, context={'request': request})
        return Response(serializer.data)


class TimelineViewSet(viewsets.ModelViewSet):
    """时间片，对具体的时间片，可以报名（apply）或者取消报名（cancel）"""
    queryset = Timeline.objects.all()
    serializer_class = TimelineSerializerPUBLIC

    def list(self, request):
        queryset = Timeline.objects.filter(user=request.user)
        serializer = TimelineSerializerUSER(
            queryset, many=True, context={'request': request})
        return Response(serializer.data)

    def get_permissions(self):
        if self.action in ['list', 'retrieve', 'apply', 'cancel']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

    @action(detail=True, methods=['GET'])
    def cancel(self, request, pk=None):
        """取消报名该时间段"""
        a = self.get_object()
        if a.user == request.user:
            a.user = None
            a.save()
            print(dir(a))
            print(a)
            return Response({"msg": "成功取消"})

        return Response({"msg": "you are not the user"})

    @action(detail=True, methods=["GET"])
    def apply(self, request, pk=None):
        """报名该时间段"""
        a = self.get_object()
        if a.user == None:
            a.user = request.user
            a.save()
            return Response({"msg": "报名成功"})
        elif a.user == request.user:
            return Response({"msg": "已报名"})
        return Response({"msg": "无法报名"})


# class InterviewTimelineViewSetADMIN(viewsets.ModelViewSet):
#     queryset = InterviewTimeline.objects.all()
#     serializer_class = InterviewTimelineSerializerADMIN


# class TimelineViewSetADMIN(viewsets.ModelViewSet):
#     queryset = Timeline.objects.all()
#     serializer_class = TimelineSerializerADMIN


class InStateViewSet(viewsets.ModelViewSet):
    queryset = InState.objects.all()
    serializer_class = InStateSerializerADMIN
