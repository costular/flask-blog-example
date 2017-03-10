#!/usr/bin/env python
# -*- coding: utf-8 -*-
from common.api import api
from users.resources import Authenticate

__author__ = 'costular'


api.add_resource(Authenticate, '/authenticate')
