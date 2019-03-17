from django.shortcuts import render
from .models import UserProfile, Club, UserProfileClub, Membership
from rest_framework.response import Response
from rest_framework import viewsets, views
from rest_framework.permissions import IsAuthenticated
from .serializer import CurrentUserProfileSerializer, \
    UserProfileSerializer, ClubSerializer, \
    UserProfileClubSerializer, MembershipSerializer
from timelines.serializer import InterviewSerializer
from timelines.models import Interview
from rest_framework.decorators import action
from django.db.models import Q
# Create your views here.

# user类别


class CurrentUserViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = CurrentUserProfileSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user

    def list(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


# TODO 应该在未来禁用
class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


# public 类别
class ClubViewSet(viewsets.ModelViewSet):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer

    @action(detail=True, methods=['GET'])
    def interview(self, request, pk=None):
        # edit_finish == False 必不可见
        # is_public 控制 无关系情况下是否可见
        # in_state 控制有关系情况下
        queryset = Interview.objects.filter(club__pk=pk,
                                            edit_finish=True)
        me = UserProfile.objects.get(username=request.user)
        userProfileClub = UserProfileClub.objects.get(
            userProfile=request.user, club__pk=pk)

        if userProfileClub and userProfileClub.membership:
            # if membership exist
            queryset = queryset.filter(
                in_state__membership=userProfileClub.membership)
        else:
            queryset = queryset.filter(is_public=True)

        serializer = InterviewSerializer(
            queryset, many=True, context={'request': request}
        )
        return Response(serializer.data)

# user 类别


class UserProfileClubViewSet(viewsets.ModelViewSet):
    queryset = UserProfileClub.objects.all()
    serializer_class = UserProfileClubSerializer

    def list(self, request):
        queryset = UserProfileClub.objects.filter(userProfile=request.user)
        serializer = UserProfileClubSerializer(
            queryset, many=True, context={'request': request})
        return Response(serializer.data)


class MembershipViewSet(viewsets.ModelViewSet):
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer
