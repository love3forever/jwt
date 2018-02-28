#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-28 10:40:05
# @Author  : wangmengcn (eclipse_sv@163.com)
# @Site    : https://eclipsesv.com
from pymongo import MongoClient
mongodb_config = {
    'host': 'localhost',
    'port': 27017
}


client = MongoClient(**mongodb_config)
