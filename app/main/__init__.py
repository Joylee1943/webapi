#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 使用蓝本是因为调用create_app()之后才能使用app.route修饰器，这时路由定义的就太晚
# 蓝本中的路由处于休眠状态，直到蓝本注册到程序上，路由才真正成为程序的一部分
from flask import Blueprint

main = Blueprint('main', __name__)

from . import errors,views