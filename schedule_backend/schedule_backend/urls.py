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
from wechattoken import views
from users import views_user as user_view
from timelines import views_user as timeline_view

from users import views_admin as user_view_admin
from timelines import views_admin as timeline_view_admin

# 普通用户接口
router = routers.DefaultRouter()
router.register('user', user_view.CurrentUserViewSet)
router.register('club', user_view.ClubViewSet)
router.register('membership', user_view.MembershipViewSet)


# 管理者接口
router_admin = routers.DefaultRouter()
router_admin.register('user', user_view_admin.UserProfileViewSet)
router_admin.register('club', user_view_admin.ClubViewSet)
router_admin.register('membership', user_view_admin.MembershipViewSet)
router_admin.register('interview', timeline_view_admin.InterviewViewSet)
router_admin.register('interviewTimeline',
                      timeline_view_admin.InterviewTimelineViewSet)
router_admin.register('timeline', timeline_view_admin.TimelineViewSet)
router_admin.register('instate', timeline_view_admin.InStateViewSet)

# Wire up our API using automatic URL routing
# additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),  # get current user
    path(r'api/', include(router.urls)),
    path(r'api-admin/', include(router_admin.urls)),
    url(r'api-auth/', include('rest_framework.urls'), name='rest_framework'),
    path(r'api_token_auth/', views.obtain_auth_token),
]
