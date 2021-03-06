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
            abort(400)

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


@rest_user_control.resource('/passwordreset')
class PasswordReset(Resource):
    """用户重置密码"""
    @jwt_required()
    def post(self):
        reset_data = request.get_json()
        current_user = current_identity
        try:
            username = current_user.username
            password = reset_data['password']
            new_password = reset_data['newpassword']
        except Exception as e:
            print(str(e))
            abort(400)
        msg = User.reset_password(username, password, new_password)
        if msg.get('error_code'):
            print(msg)
            abort(400, message=msg.get('msg'))
        return make_response(jsonify(msg))


@rest_user_control.resource('/logout')
class UserLogOut(Resource):
    """用户登出操作"""
    @jwt_required()
    def post(self):
        current_user = current_identity
        try:
            username = current_user.username
        except Exception as e:
            print(str(e))
            abort(400)
        msg = User.reset_token_last_modified(username)
        if msg.get('error_code'):
            abort(400)
        return make_response(jsonify(msg))


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
