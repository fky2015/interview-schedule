from django.shortcuts import render
from .models import UserProfile, Club
from rest_framework import viewsets
from .serializer import UserProfileSerializer, ClubSerializer
# Create your views here.


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class ClubViewSet(viewsets.ModelViewSet):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer

