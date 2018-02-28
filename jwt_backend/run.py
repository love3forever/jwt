#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017/12/4
# @Author  : wangmengcn@eclipse_sv@163.com
from create_app import create_app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=12345, debug=True)
