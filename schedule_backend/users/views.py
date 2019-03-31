from django.shortcuts import render
from .models import UserProfile, Club, UserProfileClub, Membership
from rest_framework.response import Response
from rest_framework import viewsets, views
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from .serializer import UserProfileSerializerUSER, \
    UserProfileSerializerUSER, ClubSerializerPUBLIC, \
    UserProfileClubSerializerUSER, MembershipSerializerUSER, \
    ClubSerializerADMIN
from timelines.serializer import InterviewSerializerPUBLIC, \
    TimelineSerializerUSER
from timelines.models import Interview, Timeline
from rest_framework.decorators import action, api_view
from django.db.models import Q
# Create your views here.

# user类别


class CurrentUserViewSet(viewsets.ModelViewSet):
    """获得当前用户信息"""
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializerUSER
    permission_classes = (IsAuthenticated,)

    # TODO: set password method

    def get_permissions(self):
        if self.action in ['destroy']:
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

    def get_object(self):
        return self.request.user

    def list(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @action(detail=False, methods=['GET'])
    def timeline(self, request, pk=None):
        """属于该用户的面试时间片"""
        queryset = Timeline.objects.filter(user=request.user)
        serializer = TimelineSerializerUSER(
            queryset, many=True, context={'request': request})
        return Response(serializer.data)

    @action(detail=False, methods=['GET'])
    def club(self, request, pk=None):
        """该用户参与的社团"""
        queryset = UserProfileClub.objects.filter(userProfile=request.user)
        serializer = UserProfileClubSerializerUSER(
            queryset, many=True, context={'request': request})
        return Response(serializer.data)


# TODO 应该在未来禁用
class UserProfileViewSetPUBLIC(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializerUSER


# public 类别
class ClubViewSet(viewsets.ModelViewSet):
    """获得所有社团，并可进一步获得某个社团的面试"""
    queryset = Club.objects.all()
    serializer_class = ClubSerializerPUBLIC

    def get_permissions(self):
        if self.action in ['list', 'retrieve', 'interview']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

    @action(detail=True, methods=['GET'])
    def interview(self, request, pk=None):
        """获得该club的所有你可见的面试"""
        # edit_finish == False 必不可见
        # is_public 控制 无关系情况下是否可见
        # in_state 控制有关系情况下
        queryset = Interview.objects.filter(club__pk=pk,
                                            edit_finish=True)
        me = UserProfile.objects.get(username=request.user)
        # get 在未取得情况下会直接excption
        userProfileClub_queryset = UserProfileClub.objects.filter(
            userProfile=me, club__pk=pk)
        if userProfileClub_queryset.count() > 0 and userProfileClub_queryset[0].membership:
            # if membership exist
            queryset = queryset.filter(
                in_state__membership=userProfileClub_queryset[0].membership)
        else:
            queryset = queryset.filter(is_public=True)

        serializer = InterviewSerializerPUBLIC(
            queryset, many=True, context={'request': request}
        )
        return Response(serializer.data)


class ClubViewSetADMIN(viewsets.ModelViewSet):
    queryset = Club.objects.all()
    serializer_class = ClubSerializerADMIN


class UserProfileClubViewSet(viewsets.ModelViewSet):
    """将被废弃"""
    queryset = UserProfileClub.objects.all()
    serializer_class = UserProfileClubSerializerUSER
    permission_classes = (AllowAny,)

    def list(self, request):
        queryset = UserProfileClub.objects.filter(userProfile=request.user)
        serializer = UserProfileClubSerializerUSER(
            queryset, many=True, context={'request': request})
        return Response(serializer.data)

    # def destroy(self, request, *args, **kwargs):
    #     obj = self.get_object()
    #     # self.check_permissions()
        # super(UserProf)


class MembershipViewSet(viewsets.ModelViewSet):
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializerUSER

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]
