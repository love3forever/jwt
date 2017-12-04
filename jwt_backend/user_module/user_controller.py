#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017/12/4
# @Author  : wangmengcn@eclipse_sv@163.com

from flask_restful import Api, Resource, abort, request
from flask import make_response, jsonify
from flask.blueprints import Blueprint
from flask_jwt import jwt_required, current_identity

from .user_model import User

bp_user_control = Blueprint(__name__, 'userControl', url_prefix='/api/v1/user')
rest_user_control = Api(bp_user_control)


@rest_user_control.resource('/register')
class UserRegister(Resource):
    """新用户注册"""

    def post(self):
        register_data = request.get_json()
        try:
            username = register_data['username']
            password = register_data['password']
        except Exception as e:
            print(str(e))
            abort(503)

        new_user = User(username, password)
        flag, msg = new_user.gen_user()
        response = {}
        if flag:
            response = {
                'error_code': 0,
                'msg': 'user registered successfully'
            }
        else:
            if msg:
                response = {
                    'error_code': 1,
                    'msg': 'user:{} has been registered,use another username'
                }
            else:
                response = {
                    'error_code': 2,
                    'msg': 'something wrong happend'
                }
        return make_response(jsonify(response))


@rest_user_control.resource('/info')
class UserInfo(Resource):
    """用户基本信息"""

    @jwt_required()
    def get(self):
        current_user = current_identity
        response = {
            'username': current_user.username
        }
        return make_response(jsonify(response))
