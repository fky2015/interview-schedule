from django.shortcuts import render
from .models import UserProfile, Club, UserProfileClub, Membership
from rest_framework.response import Response
from rest_framework import viewsets, views
from rest_framework.permissions import IsAuthenticated
from .serializer import UserProfileSerializerUSER, \
    UserProfileSerializerUSER, ClubSerializerPUBLIC, \
    UserProfileClubSerializerUSER, MembershipSerializerUSER, \
    ClubSerializerADMIN
from timelines.serializer import InterviewSerializerPUBLIC
from timelines.models import Interview
from rest_framework.decorators import action
from django.db.models import Q
# Create your views here.

# user类别


class CurrentUserViewSetUSER(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializerUSER
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user

    def list(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


# TODO 应该在未来禁用
class UserProfileViewSetPUBLIC(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializerUSER


# public 类别
class ClubViewSetPUBLIC(viewsets.ModelViewSet):
    queryset = Club.objects.all()
    serializer_class = ClubSerializerPUBLIC

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

        serializer = InterviewSerializerPUBLIC(
            queryset, many=True, context={'request': request}
        )
        return Response(serializer.data)


class ClubViewSetADMIN(viewsets.ModelViewSet):
    queryset = Club.objects.all()
    serializer_class = ClubSerializerADMIN
    

class UserProfileClubViewSetUSER(viewsets.ModelViewSet):
    queryset = UserProfileClub.objects.all()
    serializer_class = UserProfileClubSerializerUSER

    def list(self, request):
        queryset = UserProfileClub.objects.filter(userProfile=request.user)
        serializer = UserProfileClubSerializerUSER(
            queryset, many=True, context={'request': request})
        return Response(serializer.data)


class MembershipViewSetUSER(viewsets.ModelViewSet):
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializerUSER
