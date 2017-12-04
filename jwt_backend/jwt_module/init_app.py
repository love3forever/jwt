#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017/12/4
# @Author  : wangmengcn@eclipse_sv@163.com
from datetime import timedelta

from flask import Flask
from flask_jwt import JWT

from jwt_backend.user_module.user_model import User
from jwt_backend.user_module.user_controller import bp_user_control

app = Flask(__name__)


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
        # 返回值为之后的current_identity
        return User.gen_user_by_id(user_id)
    else:
        return None


def jwt_error_handler(e):
    return "Something bad happened", 400


JWT_CONFIG = {
    'JWT_SECRET_KEY': 'jwt_secret',
    'JWT_AUTH_URL_RULE': '/api/v1/auth',
    'JWT_EXPIRATION_DELTA': timedelta(days=1)
}


def create_app():
    # jwt配置
    app.config.update(JWT_CONFIG)
    jwt = JWT(app, authenticate, identity)
    jwt.jwt_error_handler(jwt_error_handler)

    # 注册blueprint
    app.register_blueprint(bp_user_control)
    return app
