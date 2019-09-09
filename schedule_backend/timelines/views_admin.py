from django.db import transaction  # 原子性
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from users.models import Membership, UserProfileClub

from .models import InState, Interview, InterviewTimeline, Timeline
from .serializer import (InStateSerializerADMIN, InterviewSerializerADMIN,
                         InterviewTimelineSerializerADMIN,
                         TimelineSerializerADMIN)


def get_userProfile_Club(user, club):
    """retrieve relation of user and club"""
    return UserProfileClub.objects.get(userProfile=user, club=club)


class InterviewViewSet(viewsets.ModelViewSet):
    queryset = Interview.objects.all()
    serializer_class = InterviewSerializerADMIN
    # permission_classes =

    def get_permissions(self):
        if self.action in []:
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def query_restrain(self, queryset) -> queryset:
        """基本的query集合约束，非常有用"""
        return queryset.filter(club__userProfileClub__userProfile=self.request.user,
                               club__userProfileClub__membership__is_admin=True)

    def get_queryset(self):
        """list 时进行自定义的过滤，
            只列出自己管理的Club"""
        queryset = super().get_queryset()
        return self.query_restrain(queryset)

    @transaction.atomic
    def perform_create(self, serializer):
        obj = serializer.save()

        # 如果没有相应权限，会在此步报错
        UserProfileClub.objects.get(userProfile=self.request.user,
                                    club=obj.club, membership__is_admin=True)

        mem = Membership.objects.filter(club=obj.club).first()
        obj.out_state = mem
        print(mem)
        obj.save()

    # 归 query_restrain 管理
    # def update(self, request, *args, **kwargs):
    #     """有权限更新的人才能更新"""
    #     """不好测试"""
    #     club_user = UserProfileClub.objects.get(
    #         userProfile=self.request.user, club_interview=self.get_object(),
    #         membership__is_admin=True)

    #     return super().update(request, *args, **kwargs)

    @action(detail=True, methods=['GET'])
    def interviewTimeline(self, request, pk=None):
        """返回该面试下的所有面试表"""
        interview = self.get_object()
        queryset = InterviewTimeline.objects.filter(interview=interview)

        serializer = InterviewTimelineSerializerADMIN(
            queryset, many=True, context={'request': request}
        )
        return Response(serializer.data)

    @action(detail=True, methods=['GET'])
    def instate(self, request, pk):
        """返回该面试的准入状态"""
        interview = self.get_object()
        queryset = InState.objects.filter(interview=interview)

        serializer = InStateSerializerADMIN(
            queryset, many=True, context={'request': request}
        )
        return Response(serializer.data)


class InterviewTimelineViewSet(viewsets.ModelViewSet):
    queryset = InterviewTimeline.objects.all()
    serializer_class = InterviewTimelineSerializerADMIN
    permission_classes = [IsAuthenticated]

    def query_restrain(self, queryset):
        """基本的query集合约束，非常有用"""
        return queryset.filter(interview__club__userProfileClub__userProfile=self.request.user,
                               interview__club__userProfileClub__membership__is_admin=True)

    def get_queryset(self):
        """list 时进行自定义的过滤，
            只列出自己管理的Club"""
        queryset = super().get_queryset()
        return self.query_restrain(queryset)

    @transaction.atomic
    def perform_create(self, serializer):
        obj = serializer.save()

        # 如果没有相应权限，会在此步报错
        UserProfileClub.objects.get(userProfile=self.request.user,
                                    club=obj.interview.club, membership__is_admin=True)

    @action(detail=True, methods=['GET'])
    def timeline(self, request, pk=None):
        obj = self.get_object()
        queryset = Timeline.objects.filter(interviewTimeline=obj)
        serializer = TimelineSerializerADMIN(
            queryset, many=True, context={'request': request})
        return Response(serializer.data)


class CreateListModelMixin(object):

    def get_serializer(self, *args, **kwargs):
        """ if an array is passed, set serializer to many """
        if isinstance(kwargs.get('data', {}), list):
            kwargs['many'] = True
        return super(CreateListModelMixin, self).get_serializer(*args, **kwargs)


class TimelineViewSet(viewsets.ModelViewSet, CreateListModelMixin):
    queryset = Timeline.objects.all()
    serializer_class = TimelineSerializerADMIN
    permission_classes = [IsAuthenticated]

    def query_restrain(self, queryset):
        """基本的query集合约束，非常有用"""
        return queryset.filter(interviewTimeline__interview__club__userProfileClub__userProfile=self.request.user,
                               interviewTimeline__interview__club__userProfileClub__membership__is_admin=True)

    def get_queryset(self):
        """list 时进行自定义的过滤，
            只列出自己管理的Club"""
        queryset = super().get_queryset()
        return self.query_restrain(queryset)

    def get_serializer(self, *args, **kwargs):
        """ if an array is passed, set serializer to many """
        if isinstance(kwargs.get('data', {}), list):
            kwargs['many'] = True
        return super().get_serializer(*args, **kwargs)

    @transaction.atomic
    def perform_create(self, serializer):
        obj = serializer.save()

        # 如果没有相应权限，会在此步报错
        UserProfileClub.objects.get(userProfile=self.request.user,
                                    club=obj.interviewTimeline.interview.club, membership__is_admin=True)


class InStateViewSet(viewsets.ModelViewSet):
    queryset = InState.objects.all()
    serializer_class = InStateSerializerADMIN

    def get_permissions(self):
        if self.action in []:
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def query_restrain(self, queryset) -> queryset:
        """基本的query集合约束，非常有用"""
        return queryset.filter(interview__club__userProfileClub__userProfile=self.request.user,
                               interview__club__userProfileClub__membership__is_admin=True)

    def get_queryset(self):
        """list 时进行自定义的过滤，
            只列出自己管理的Club"""
        queryset = super().get_queryset()
        return self.query_restrain(queryset)

    # @transaction.atomic
    # def perform_create(self, serializer):
    #     obj = serializer.save()

        # # TODO: 也可以整合为一个permission类
        # # 如果没有相应权限，会在此步报错
        # UserProfileClub.objects.get(userProfile=self.request.user,
        #                             club=obj.interview.club, membership__is_admin=True)
