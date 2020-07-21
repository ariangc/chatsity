#!/usr/bin/env python

"""
    security.py
    ----------
    This module implements the necesary functions to verify the
    authenticity of the user when sending a request. It uses
    HTTP Basic Authentication for that purpose.
"""

__author__ = "Arian Gallardo"

from flask_httpauth import HTTPBasicAuth
from flask_restful import Resource
from flask import g
from models.user import User
from werkzeug.security import check_password_hash

auth = HTTPBasicAuth()

@auth.verify_password
def Verify_password(email_or_token, password):
    """ Verifies token or password sent by the requester.

        :type email_or_token: str
        :param email_or_token: Email or token sent by the requester.

        :type password: str
        :param password: Encoded password to be verified.
    """

    user = User.VerifyAuthToken(email_or_token)
    if not user:
        user = User.query.filter_by(email=email_or_token).first()
        if not user or not check_password_hash(user.password, password):
            return False
    
    g.user = user
    return True

class AuthRequiredResource(Resource):
    method_decorators = [auth.login_required]
