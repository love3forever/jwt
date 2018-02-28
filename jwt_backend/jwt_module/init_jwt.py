#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017/12/4
# @Author  : wangmengcn@eclipse_sv@163.com
from datetime import timedelta, datetime
from user_module.user_model import User


# JWT相关配置
def authenticate(username, password):
    user = User(username, password)
    flag, _ = user.check_password()
    if flag:
        return user
    else:
        return None


def identity(payload):
    if payload:
        user_id = payload['identity']
        token_generated_at = payload['iat']
        print(payload)
        print('use this function to identity user info')
        target_user = User.get_user_by_id(user_id)
        # 用以确保用户重置密码之后之前的token不被认证
        if target_user.is_token_outofdate(
            datetime.utcfromtimestamp(token_generated_at)
        ):
            print('token has expired')
            return None
        # 返回值为之后的current_identity
        return target_user
    else:
        return None


def jwt_error_handler(e):
    return "Something bad happened", 400


JWT_CONFIG = {
    'JWT_SECRET_KEY': 'jwt_secret',
    'JWT_AUTH_URL_RULE': '/api/v1/auth',
    'JWT_EXPIRATION_DELTA': timedelta(days=1)
}
