# -*- coding:utf-8 -*-
import requests
from django.conf import settings
from rest_framework import serializers
from django.utils.translation import ugettext_lazy as _



class AuthTokenSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=32, required=True, label=_('Code'))
    username = serializers.CharField(max_length=32)
    password = serializers.CharField(max_length=32)

    def validate(self, attrs):
        code = attrs.get('code')
        # 获取用户名
        username = attrs.get('username')
        attrs['username'] = username.strip()
        # password = attrs.get('password')
        result = self._credentials_validation(code)

        attrs['openid'] = result['openid']
        attrs['session_key'] = result['session_key']
        return attrs

    @staticmethod
    def _credentials_validation(code):
        # 成功拿到openid和session_key并返回
        req_params = {
            'appid': settings.WECHAT_APPID,
            'secret': settings.WECHAT_SECRET,
            'js_code': code,
            'grant_type': 'authorization_code'
        }
        url = 'https://api.weixin.qq.com/sns/jscode2session'

        response = requests.get(url, params=req_params)
        result = response.json()

        if 'errcode' in result:
            msg = _(result['errmsg'])
            raise serializers.ValidationError(msg, code='authorization')

        return result
