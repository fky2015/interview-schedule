from django.shortcuts import render
from .models import InterviewTimeline, Interview, Timeline,\
    InState
from .serializer import InStateSerializerADMIN, \
    InterviewSerializerADMIN, InterviewTimelineSerializerADMIN, \
    TimelineSerializerADMIN
from users.models import Membership
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAdminUser
from django.db import transaction  # 原子性


class InterviewViewSet(viewsets.ModelViewSet):
    queryset = Interview.objects.all()
    serializer_class = InterviewSerializerADMIN


class InterviewTimelineViewSet(viewsets.ModelViewSet):
    queryset = InterviewTimeline.objects.all()
    serializer_class = InterviewTimelineSerializerADMIN


class TimelineViewSet(viewsets.ModelViewSet):
    queryset = Timeline.objects.all()
    serializer_class = TimelineSerializerADMIN

class InStateViewSet(viewsets.ModelViewSet):
    queryset = InState.objects.all()
    serializer_class = InStateSerializerADMIN