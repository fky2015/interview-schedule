from django.shortcuts import render
from .models import InterviewTimeline, Interview, Timeline
from .serializer import InterviewSerializer, InterviewTimelineSerializer, TimelineSerializer
from rest_framework import viewsets


# Create your views here.


class InterviewViewSet(viewsets.ModelViewSet):
    queryset = Interview.objects.all()
    serializer_class = InterviewSerializer

class InterviewTimelineViewSet(viewsets.ModelViewSet):
    queryset = InterviewTimeline.objects.all()
    serializer_class = InterviewTimelineSerializer

class TimelineViewSet(viewsets.ModelViewSet):
    queryset = Timeline.objects.all()
    serializer_class = TimelineSerializer

    

