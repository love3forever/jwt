#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-28 10:33:27
# @Author  : wangmengcn (eclipse_sv@163.com)
# @Site    : https://eclipsesv.com
from flask import Flask
from flask_jwt import JWT
from user_module.user_controller import bp_user_control
from jwt_module.init_jwt import (
    JWT_CONFIG, authenticate, identity, jwt_error_handler
)


app = Flask(__name__)


def create_app():
    # jwt配置
    app.config.update(JWT_CONFIG)
    jwt = JWT(app, authenticate, identity)
    jwt.jwt_error_handler(jwt_error_handler)

    # 注册blueprint
    app.register_blueprint(bp_user_control)

    @app.after_request
    def after_request(resp):
        resp.headers['Access-Control-Allow-Origin'] = '*'
        resp.headers['Access-Control-Allow-Methods'] = '*'
        resp.headers[
            'Access-Control-Allow-Headers'] = '*'
        resp.headers['Content-Type'] = 'application/json;charset=UTF-8'
        return resp

    return app
