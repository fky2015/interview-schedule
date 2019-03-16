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
        queryset = Interview.objects.filter(pk=pk)
        # 如果该面试同意公开，或者自己与社团的关系符合在in_state中，才会显示
        # TODO
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
