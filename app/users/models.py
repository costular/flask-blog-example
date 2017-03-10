#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime, timedelta

import jwt
from common.db import db
from flask import current_app
from werkzeug.security import generate_password_hash, check_password_hash

__author__ = 'costular'


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True)

    # Autenticación
    email = db.Column(db.String(100), unique=True, nullable=False)
    hash_password = db.Column('password', db.String(255), nullable=True)
    reset_password_token = db.Column(db.String(100), default='', nullable=True)
    token_expiration = db.Column(db.DateTime(), nullable=True)

    # Info
    name = db.Column(db.String(55), nullable=False, default='')
    avatar_url = db.Column(db.Text())
    registered_by = db.Column(db.Enum('facebook', 'twitter', 'google', 'email'))
    registered_at = db.Column(db.DateTime(), default=datetime.now())
    last_login_ip = db.Column(db.String(45))
    login_try_count = db.Column(db.Integer())

    is_admin = db.Column(db.Boolean(), default=False)

    def __init__(self, email, password):
        self.email = email
        self.hash_password = generate_password_hash(password)

    @property
    def password(self):
        return self.hash_password

    @password.setter
    def password(self, password):
        self.hash_password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.hash_password, password)

    def is_admin(self):
        return self.is_admin

    def generate_auth_token(self, days_expiration=14): #14 días
        self.expiration_ = {
            'sub': self.id,
            'iat': datetime.utcnow(),
            'exp': datetime.utcnow() + timedelta(days=days_expiration)
        }
        payload = self.expiration_
        token = jwt.encode(payload, current_app.config['SECRET_KEY'], algorithm='HS256')
        return token

    @staticmethod
    def verify_auth_token(token):
        if 'Bearer' in token:
            token = token.replace('Bearer ' , '')
        try:
            result = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
            return User.query.get(int(result['sub']))
        except:
            return False
