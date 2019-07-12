#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

basedir=os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASKY_MAIL_SUBJECT_PREFIX = '[WebAPI]'
    FLASKY_MAIL_SENDER = 'Web API Auto'

    # 对当前环境初始化
    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG=True
    MAIL_SERVER = 'smtp.sengled.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'auto.test@sengled.com'
    MAIL_PASSWORD = 'Sengled.123'

config={
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}