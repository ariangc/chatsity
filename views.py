#!/usr/bin/env python

"""
      views.py
      ----------
      This module register all resources/services that the app will
      contain into a blueprint, which is also registered into the
      app itself.
"""

__author__ = "Arian Gallardo"

from flask import Blueprint
from flask_restful import Api, Resource

from resources.authentication import SignupResource, LoginResource, LogoutResource, VerifyTokenResource

api_blueprint = Blueprint('api', __name__)
api = Api(api_blueprint)

api.add_resource(SignupResource, '/signup')
api.add_resource(LoginResource, '/login')
api.add_resource(LogoutResource, '/logout')
api.add_resource(VerifyTokenResource, '/verify')