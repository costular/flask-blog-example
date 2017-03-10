#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Blueprint
from flask_restful import Api

__author__ = 'costular'


api = Api()
api_blueprint = Blueprint('api', __name__, url_prefix='/api')


