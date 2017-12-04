#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017/12/4
# @Author  : wangmengcn@eclipse_sv@163.com

from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
from bson import ObjectId

client = MongoClient()
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
                     'password': generate_password_hash(self.password)}
                )
            except Exception as e:
                print(str(e))
                return False, None
            else:
                return True, str(insert_result.inserted_id)

    @property
    def id(self):
        flag, _id = self.check_password()
        if flag and _id:
            return _id
        else:
            return None

    @classmethod
    def gen_user_by_id(cls, user_id):
        _id = ObjectId(user_id)
        user = col.find_one({"_id": _id})
        if user is not None:
            return cls(user['username'], user['password'])
        else:
            return None
