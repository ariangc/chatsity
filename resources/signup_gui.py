#!/usr/bin/env python

"""
    signup_gui.py
    ----------
    This module implements the necessary functions to return and
    render a HTML template to let a user signup into the platform.
"""

__author__ = "Arian Gallardo"

from flask import make_response, render_template
from flask_restful import Resource

class SignupGUIResource(Resource):
    "Resource to return signup HTML GUI."
    def get(self):
        """ GET request handler for SignupGUIResource. Retrieves
            an HTML template to let the user signup to the platform.
        """
        return make_response(render_template('signup.html'))