from django.shortcuts import render
from .serializer import FeedSerializers
from .models import Feed
from rest_framework import viewsets
# Create your views here.


class FeedViewSet(viewsets.ModelViewSet):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializers