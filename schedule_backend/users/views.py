from django.shortcuts import render
from .models import UserProfile, Club,UserProfileClub
from rest_framework.response import Response
from rest_framework import viewsets, views
from rest_framework.permissions import IsAuthenticated
from .serializer import UserProfileSerializer, ClubSerializer, UserProfileClubSerializer
from rest_framework.decorators import action
# Create your views here.


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    @action(detail=False)
    def current(self, request):
        serializer = UserProfileSerializer(
            request.user, context={"request": request})
        return Response(serializer.data)

    @action(detail=False)
    def my_club(self, request):
        pass


class ClubViewSet(viewsets.ModelViewSet):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer


class UserProfileClubViewSet(viewsets.ModelViewSet):
    queryset = UserProfileClub.objects.all()
    serializer_class = UserProfileClubSerializer

class CurrentUserView(views.APIView):

    # 解决报错
    # Cannot apply DjangoModelPermissionsOrAnonReadOnly on a view
    # that does not set `.queryset` or have a `.get_queryset()` method.
    permission_classes = (IsAuthenticated,)

    # 按照要求返回当前user TODO 不知道这几个方法速度差异怎样
    def get(self, request):
        serializer = UserProfileSerializer(
            request.user, context={"request": request})
        return Response(serializer.data)
