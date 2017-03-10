#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask_restful import Resource, reqparse, abort
from users.models import User

__author__ = 'costular'


class Authenticate(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email', help='Nombre de usuario')
        parser.add_argument('password', help=u'Contraseña del usuario')
        args = parser.parse_args()
        email = args['email']
        password = args['password']
        user = User.query.filter_by(email=email).first()

        if not user:
            abort(401)

        if user.verify_password(password):
            return {'token': user.generate_auth_token()}
        else:
            return abort(401)
