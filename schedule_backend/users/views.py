from django.shortcuts import render
from .models import UserProfile, Club
from rest_framework.response import Response
from rest_framework import viewsets, views
from rest_framework.permissions import IsAuthenticated
from .serializer import UserProfileSerializer, ClubSerializer
# Create your views here.


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class ClubViewSet(viewsets.ModelViewSet):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer


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
