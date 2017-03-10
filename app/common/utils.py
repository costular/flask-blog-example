#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask.json import jsonify

__author__ = 'costular'


class Utils(object):

    @staticmethod
    def unauthorized(message):
        response = jsonify({'message': message})
        response.status_code = 401
        return response

    @staticmethod
    def missing_header(header):
        headers_missed = ','.join(header)
        response = jsonify({'message': 'headers miss: %s' % headers_missed})
        response.status_code = 400
        return response
