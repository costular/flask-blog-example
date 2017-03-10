#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'costular'


class Config(object):
    SECRET_KEY = 'unaahíquedeberemoscambiarensudebidomomento'

    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class Development(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://flask:flask@localhost/flaskpress'


class Production(Config):
    pass


config = {
    'development': Development,
    'production': Production,
    'default': Development
}
