from django.contrib.auth import get_user_model
from rest_framework import parsers, renderers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions

from wechattoken.models import Token
from wechattoken.serializers import AuthTokenSerializer
from users.serializer import UserProfileSerializerADMIN, UserProfileSerializerUSER


import logging

User = get_user_model()

logger = logging.getLogger('django')


class ObtainAuthToken(APIView):
    """生成并返回Token

    请求和响应均为json类型.
    通过小程序post请求发送code, 经AuthTokenSerializer验证后返回
    openid和session_key.

    使用用户标识openid生成一个user实例, 方便视图对用户权限的管理.
    """
    serializer_class = AuthTokenSerializer
    parser_classes = (parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        openid = serializer.validated_data['openid']
        session_key = serializer.validated_data['session_key']

        # # 如果是新注册的用户
        # if username:
        #     # 只有新注册，或者要做关联的时候才会有username
        #     user, is_new_one = User.objects.get_or_create(
        #         username=username)
        #     # 新注册
        #     if is_new_one:
        #         user.set_password(password)
        #     # 关联
        #     else:
        #         if user.check_password(password):
        #             raise PermissionError("wrong username or password!")
        try:
            user = User.objects.get(
                username=openid,
                password=openid,
            )
            # defaults={'password': openid}

        except User.DoesNotExist:
            # 可以新建用户
            user_serializer = UserProfileSerializerUSER(data=request.data)
            user_serializer.is_valid(raise_exception=True)
            data = {**user_serializer.validated_data}
            data['username'] = openid
            data['password'] = openid
            user = User.objects.create(**data)

        token, _ = Token.objects.update_or_create(
            user=user, openid=openid,
            defaults={'session_key': session_key, 'key': ''}
        )

        serializer = UserProfileSerializerUSER(
            user, context={'request': request}
        )
        return Response(
            {
                'token': token.key,
                'user': serializer.data
            })


obtain_auth_token = ObtainAuthToken.as_view()
