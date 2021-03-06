'''
@Date: 2019-08-10 22:12:19
@LastEditors: Feng Kaiyu
@LastEditTime: 2019-08-10 22:20:16
@Description: urls
@Author: Feng Kaiyu
'''
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


from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
# 普通用户接口
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, routers, serializers, viewsets

from timelines import views_admin as timeline_view_admin
from timelines import views_user as timeline_view
from users import views_admin as user_view_admin
from users import views_user as user_view
from wechattoken import views

from .view import management, redirect_view

router = routers.DefaultRouter()
router.register('user', user_view.CurrentUserViewSet, basename='userprofile')
router.register('club', user_view.ClubViewSet, basename='club')
router.register('membership', user_view.MembershipViewSet,
                basename='membership')
router.register('interview', timeline_view.InterviewViewSet,
                basename='interview')
router.register('interviewTimeline',
                timeline_view.InterviewTimelineViewSet, basename='interviewtimeline')
router.register('timeline', timeline_view.TimelineViewSet,
                basename='timeline')


# 管理者接口
router_admin = routers.DefaultRouter()
# UserProfileClub 目前是测试阶段为了暴露相关接口给admin
router_admin.register(
    'user-club', user_view.UserProfileClubViewSet)
router_admin.register(
    'user', user_view_admin.UserProfileViewSet, basename="admin-user")
router_admin.register('club', user_view_admin.ClubViewSet,
                      basename="admin-club")
router_admin.register(
    'membership', user_view_admin.MembershipViewSet, basename="admin-membership")
router_admin.register(
    'interview', timeline_view_admin.InterviewViewSet, basename="admin-interview")
router_admin.register('interviewTimeline',
                      timeline_view_admin.InterviewTimelineViewSet, basename="admin-interviewtimeline")
router_admin.register(
    'timeline', timeline_view_admin.TimelineViewSet, basename="admin-timeline")
router_admin.register(
    'instate', timeline_view_admin.InStateViewSet, basename="admin-instate")

# Wire up our API using automatic URL routing
# additionally, we include login URLs for the browsable API.
urlpatterns = [
    path(r'', redirect_view),
    path(r'manage/', management),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),  # get current user
    path(r'api/', include(router.urls)),
    path(r'api-admin/', include(router_admin.urls)),
    url(r'api-auth/', include('rest_framework.urls'), name='rest_framework'),
    # url(r'^rest-auth/', include('rest_auth.urls')),
    path(r'api_token_auth/', views.obtain_auth_token),
]


schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns += [
    url(r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger',
                                           cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc',
                                         cache_timeout=0), name='schema-redoc'),
]
# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns = [
#         path('__debug__/', include(debug_toolbar.urls)),

#         # For django versions before 2.0:
#         # url(r'^__debug__/', include(debug_toolbar.urls)),

#     ] + urlpatterns
