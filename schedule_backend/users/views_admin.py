from django.db import transaction  # 原子性
from django.db.models import Q
from django.shortcuts import render
from rest_framework import views, viewsets
from rest_framework.decorators import action, api_view
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from timelines.models import Interview, Timeline
from timelines.serializer import InterviewSerializerADMIN

from .models import Club, Membership, UserProfile, UserProfileClub
from .serializer import (ClubSerializerADMIN, MembershipSerializerADMIN,
                         UserProfileSerializerADMIN)
from django.db.models import Prefetch


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializerADMIN

    def get_permissions(self):
        if self.action in ['destroy', 'create', 'update']:
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    @action(detail=False, methods=['GET'])
    def owned_clubs(self, request, pk=None):
        """自己是哪些社团的管理员"""
        queryset = UserProfileClub.objects.filter(
            userProfile=request.user, membership__is_admin=True)
        queryset = [q.club for q in queryset]
        print(queryset)
        print(type(queryset))
        serializer = ClubSerializerADMIN(
            queryset, many=True,  context={'request': request}
        )
        return Response(serializer.data)


# 有机会的话整合一下吧

def get_userProfile_Club(user, club):
    """retrieve relation of user and club"""
    return UserProfileClub.objects.get(userProfile=user, club=club)


class ClubViewSet(viewsets.ModelViewSet):
    serializer_class = ClubSerializerADMIN

    def get_permissions(self):
        if self.action in ['destroy']:
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def update(self, request, *args, **kwargs):
        """有权限更新的人才能更新"""
        instance = self.get_object()
        club_user = get_userProfile_Club(request.user, instance)
        if club_user.membership.is_admin:
            return super().update(request, *args, **kwargs)
        else:
            return Response({"msg": "denied"})

    @action(detail=True, methods=['GET'])
    def interview(self, request, pk=None):
        """获得所有的面试与面试表"""
        queryset = Interview.objects.filter(club__pk=pk)

        serializer = InterviewSerializerADMIN(
            queryset, many=True, context={'request': request
                                          }
        )
        return Response(serializer.data)

    @transaction.atomic
    def perform_create(self, serializer):
        """默认创建社团管理员和普通用户两种角色，会默认建立自己与社团的管理员关系"""
        # transaction 保持事务原子性
        serializer.save()
        print("save success")
        # 最笨的办法，查找，然后创建
        club = Club.objects.filter(name=self.request.data['name'])[0]
        user = self.get_user()
        adminer = Membership(club=club, name="admin",
                             is_admin=True)
        common_user = Membership(club=club, name="user")
        adminer.save()
        common_user.save()
        print(user)
        # 这里的user或许可以优化，不用取出user
        UserProfileClub(userProfile=user, club=club, membership=adminer).save()

    def get_user(self):
        """得到用户自己"""
        return self.request.user

    def query_restrain(self, queryset):
        """基本的query集合约束，非常有用"""
        return queryset.filter(userProfileClub__userProfile=self.request.user, userProfileClub__membership__is_admin=True)

    # list行为改变后，retreive也会改变 欧耶
    # def get_object_or_404(self, queryset, *filter_args, **filter_kwargs):
    #     """被get_object调用，用于自定义retrieve"""
    #     queryset = self.query_restrain(queryset)
    #     return super().get_object_or_404(queryset, *filter_args, **filter_kwargs)

    def get_queryset(self):
        """list 时进行自定义的过滤，
            只列出自己管理的Club"""
        queryset = Club.objects.all()
        return self.query_restrain(queryset)

    @action(detail=True, methods=['GET'])
    def membership(self, request, pk=None):
        """当前社团拥有的所有membership"""
        queryset = Membership.objects.filter(club=self.get_object())
        serializer = MembershipSerializerADMIN(
            queryset, many=True, context={'request': request}
        )
        return Response(serializer.data)

    @action(detail=True, methods=['GET'])
    def applicants(self, request, pk: int):
        """获得当前社团所有报名成员"""
        # queryset = UserProfile.objects.prefetch_related(Prefetch(
        #     'userProfileClub',queryset=UserProfileClub.objects.filter(club=self.get_object())
        # )).filter(userProfileClub = )
        queryset = UserProfile.objects.prefetch_related(Prefetch(
            'userProfileClub', queryset=UserProfileClub.objects.filter(club=self.get_object())
        )).filter(
            timeline__interviewTimeline__interview__club=self.get_object()
        )
        serializer = UserProfileSerializerADMIN(
            queryset, many=True, context={'request': request}
        )
        return Response(serializer.data)

    @action(detail=True, methods=['GET'])
    def members(self, request, pk: int):
        """获得当前社团所有有关联的成员"""
        queryset = UserProfile.objects.prefetch_related(Prefetch(
            'userProfileClub', queryset=UserProfileClub.objects.filter(club=self.get_object())
        )).filter(userProfileClub__club=self.get_object())
        serializer = UserProfileSerializerADMIN(
            queryset, many=True, context={'request': request}
        )
        return Response(serializer.data)


class MembershipViewSet(viewsets.ModelViewSet):
    # queryset = Membership.objects.all()
    serializer_class = MembershipSerializerADMIN

    def get_permissions(self):
        if self.action in ['list']:
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def query_restrain(self, queryset):
        """基本的query集合约束，非常有用"""
        return queryset.filter(club__userProfileClub__userProfile=self.request.user,
                               club__userProfileClub__membership__is_admin=True)

    def get_queryset(self):
        """list 时进行自定义的过滤，
            只列出自己管理的Club"""
        queryset = Membership.objects.all()
        return self.query_restrain(queryset)

    # def perform_create(self, serializer: MembershipSerializerADMIN):
    #     # print(serializer.validated_data)
    #     CreateModelMixin.create(self, serializer)
