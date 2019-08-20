#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = 'hard to guess'  # 一些敏感信息也可以放入环境变量获取
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASKY_MAIL_SUBJECT_PREFIX = '[WebAPI]'
    FLASKY_MAIL_SENDER = 'Web API Auto'

    # 对当前环境初始化，基类中的init_app()为空
    @staticmethod
    def init_app(app):
        pass


# 可以对环境做不同的配置
class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'smtp.sengled.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'auto.test@sengled.com'
    MAIL_PASSWORD = 'Sengled.123'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


# 配置多个环境，默认为为开发环境
config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
