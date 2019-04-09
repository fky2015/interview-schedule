from django.shortcuts import render
from .models import UserProfile, Club, UserProfileClub, Membership
from rest_framework.response import Response
from rest_framework import viewsets, views
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from .serializer import UserProfileSerializerADMIN, \
    ClubSerializerADMIN, MembershipSerializerADMIN

from timelines.models import Interview, Timeline
from rest_framework.decorators import action, api_view
from django.db.models import Q
from django.db import transaction  # 原子性


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializerADMIN


class ClubViewSet(viewsets.ModelViewSet):
    queryset = Club.objects.all()
    serializer_class = ClubSerializerADMIN


class MembershipViewSet(viewsets.ModelViewSet):
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializerADMIN
