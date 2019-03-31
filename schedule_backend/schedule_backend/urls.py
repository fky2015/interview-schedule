"""schedule_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers, serializers, viewsets
from users import views as user_view
from timelines import views as timeline_view

router = routers.DefaultRouter()
# public 共有信息
# router.register('public/users', user_view.UserProfileViewSetPUBLIC)
router.register('club', user_view.ClubViewSet)
router.register('interview', timeline_view.InterviewViewSet)
router.register('interviewTimeline',
                timeline_view.InterviewTimelineViewSet)
router.register('timeline', timeline_view.TimelineViewSet)


# user 用户自己的信息
router.register('user', user_view.CurrentUserViewSet)
router.register('membership', user_view.MembershipViewSet)
router.register('userProfileClub', user_view.UserProfileClubViewSet)

# # club 后台管理者相关的
router.register('instate', timeline_view.InStateViewSet)
# router.register('admin/club', user_view.ClubViewSetADMIN, basename="admin")
# router.register('admin/interview',
#                 timeline_view.InterviewViewSetADMIN, basename="admin")
# router.register('admin/interviewTimeline',
#                 timeline_view.InterviewTimelineViewSetADMIN)
# router.register('admin/timeline',
#                 timeline_view.TimelineViewSetADMIN, basename="admin")

# Wire up our API using automatic URL routing
# additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),  # get current user
    path(r'api/', include(router.urls)),
    url(r'api-auth/', include('rest_framework.urls'), name='rest_framework')
]
