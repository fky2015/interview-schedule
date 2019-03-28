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

    def get_permissions(self):
        if self.action == 'list':
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
