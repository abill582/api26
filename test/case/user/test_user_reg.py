#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/5/6 16:19
# AUTHOR    : Yanglei
# @File     : 2024/5/9.py
# @Software : PyCharm
from test.case.basecase import BaseCase
from lib.db1 import *
import json

class test_user_reg(BaseCase):
    def test_reg_ok(self):
        case_data=self.get_case_data("reg_ok")
        username=json.loads(case_data["args"])["username"]
        if check_user(username):
            del_user(username)
            self.send_request(case_data)
            self.assertTrue(check_user(username))
            del_user(username)

    def test_reg_err(self):
        # 注册用户
        case_data = self.get_case_data("reg_err")
        name = json.loads(case_data["args"])["userName"]
        # 检查环境
        if not check_user(name):
            add_user(name, "123456")
        # 数据库断言
            self.assertTrue(check_user(name))
            self.send_request(case_data)
