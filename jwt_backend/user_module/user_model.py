#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017/12/4
# @Author  : wangmengcn@eclipse_sv@163.com
from datetime import datetime

from werkzeug.security import generate_password_hash, check_password_hash
from bson import ObjectId

from db_module import client

db = client['auth']
col = db['user_module']


class User(object):
    """docstring for User"""

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def check_password(self):
        current_user = col.find_one({'username': self.username})
        if current_user:
            check_result = check_password_hash(
                current_user['password'], self.password)
            if check_result:
                return True, str(current_user['_id'])
            else:
                return False, None
        else:
            return False, None

    def gen_user(self):
        current_user = col.find_one({'username': self.username})
        if current_user is not None:
            return False, str(current_user['_id'])
        else:
            try:
                insert_result = col.insert_one(
                    {'username': self.username,
                     'password': generate_password_hash(self.password),
                     'token_last_modified': datetime.utcnow()
                     }
                )
            except Exception as e:
                print(str(e))
                return False, None
            else:
                return True, str(insert_result.inserted_id)

    @classmethod
    def reset_password(cls, username, password, new_password):
        is_old_password_correct, _ = cls(username, password).check_password()
        if is_old_password_correct:
            col.update_one({'username': username}, {
                           '$set': {
                               'password': generate_password_hash(new_password),
                               'token_last_modified': datetime.utcnow()
                           }
                           })
            return {
                "msg": "password reseted!",
                "error_code": 0
            }
        else:
            return {
                "msg": "old password is not correct!",
                "error_code": 1
            }

    @classmethod
    def reset_token_last_modified(cls, username):
        current_user = col.find_one({'username': username})
        if current_user:
            col.update_one({
                'username': username
            }, {
                '$set': {
                    'token_last_modified': datetime.utcnow()
                }
            })
            return {
                'msg': 'user logout!',
                'error_code': 0
            }
        else:
            return {
                'msg': 'failed to logout!',
                'error_code': 1
            }

    @property
    def id(self):
        flag, _id = self.check_password()
        if flag and _id:
            return _id
        else:
            return None

    @classmethod
    def get_user_by_id(cls, user_id):
        _id = ObjectId(user_id)
        user = col.find_one({"_id": _id})
        if user is not None:
            return cls(user['username'], user['password'])
        else:
            return None

    def is_token_outofdate(self, token_generated_time):
        target_user = col.find_one({'username': self.username})
        return token_generated_time < target_user.get('token_last_modified')
