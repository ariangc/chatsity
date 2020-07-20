#!/usr/bin/env python

"""
      user.py
      ----------
      This module contains the declaration of the User database model. Also,
      it handles token generation and validation for users to be used in user 
      login and user requests.
"""

__author__ = "Arian Gallardo"

from flask_login import UserMixin
from app import db
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)
from models.utils import AddUpdateDelete
from config import SECRET_KEY, TOKEN_EXP_MINUTES

class User(UserMixin, AddUpdateDelete, db.Model):
    "Class User to provide data access to information of registered users."
    __tablename__ = 'user'
    
    #class attributes
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    name = db.Column(db.String(100))
    password = db.Column(db.String(100))
    token = db.Column(db.String(512))
    messages = db.relationship("Message")

    def GenerateAuthToken(self, expiration = TOKEN_EXP_MINUTES):
        """ Generates an encoded token to handle authenticated user requests.
            
            :type expiration int
            :param expiration Expiration of token in minutes.
        """
        serializer = Serializer(SECRET_KEY, expires_in = expiration)
        return serializer.dumps({'id': self.id})

    @staticmethod
    def VerifyAuthToken(token):
        """ Verifies an encoded token to handle authenticated user requests.
            
            :type token str
            :param expiration Encoded token.
        """
        serializer = Serializer(SECRET_KEY)
        try:
            data = serializer.loads(token)
        except SignatureExpired:
            return None
        except BadSignature:
            return None

        user = User.query.get(data['id'])
        return user
