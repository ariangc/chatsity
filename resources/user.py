#!/usr/bin/env python

"""
    user.py
    ----------
    This module implements the necessary functions to read
    user information.
"""

__author__ = "Arian Gallardo"

from models.user import User
from models.message import Message
from models.chatroom import Chatroom
from flask import request
from resources.security import AuthRequiredResource
import status
import datetime

class UserResource(AuthRequiredResource):
    "Resource to manage user information."
    def get(self, id):
        """ GET request handler for UserResource. Allows reading
            information from a specific user given its id.

            In case of an error, HTTP status 400 (BAD_REQUEST) is returned.
            Else, HTTP status 200 (OK) is returned.

            :type id: int
            :param id: User id.
        """
        try:
            user = User.query.get_or_404(id)
            response = user.to_json()

            return response, status.HTTP_200_OK
        except Exception as e:
            response = {"error": str(e)}
            return response, status.HTTP_400_BAD_REQUEST