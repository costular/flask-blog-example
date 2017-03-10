#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask_script import Manager
from run import app
from flask_migrate import MigrateCommand

__author__ = 'costular'


manager = Manager(app)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()