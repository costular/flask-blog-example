#!/usr/bin/env python
# -*- coding: utf-8 -*-
from config import config
from flask import Flask
from common.db import db
from common.marshmallow import ma
from common.api import api_blueprint, api
from flask_migrate import Migrate
from users import urls

__author__ = 'costular'


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)
    ma.init_app(app)
    migrate = Migrate(app, db)
    api.init_app(api_blueprint)


    """@app.before_first_request
    def create_user():
        db.create_all()
        if User.query.count() < 1:
            user_datastore.create_user(email='diegofc@dargo.net', password='flask')
            db.session.commit()
    """

    """
    ROUTES
    """
    @app.route('/')
    def hello():
        return 'Aquí estoy para servirte 😊'

    app.register_blueprint(api_blueprint)

    return app