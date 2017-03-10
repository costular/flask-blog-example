#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app import create_app

__author__ = 'costular'


app = create_app('default')

if __name__ == '__main__':
    app.run()