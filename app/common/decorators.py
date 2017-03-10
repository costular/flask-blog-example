#!/usr/bin/env python
# -*- coding: utf-8 -*-
from common.utils import Utils
from flask import request
from functools import wraps
from users.models import User

__author__ = 'costular'


def auth_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_token = request.headers.get('Authorization')
        if not auth_token:
            return Utils.missing_header(['Authorization'])
        elif not User.verify_auth_token(auth_token):
            return Utils.unauthorized('Token no válido')
        return f(*args, **kwargs)
    return decorated


def api_admin_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_token = request.headers.get('Authorization')
        if not auth_token:
            return Utils.missing_header(['Authorization'])
        elif not User.verify_auth_token(auth_token):
            return Utils.unauthorized('Token no valido')
        if not User.verify_auth_token(auth_token).is_admin():
            return Utils.unauthorized(u'Necesitas ser administrador')
        return f(*args, **kwargs)
    return decorated
