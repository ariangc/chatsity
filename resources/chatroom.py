#!/usr/bin/env python

"""
    chatroom.py
    ----------
    This module implements the necessary functions to create and read
    chatroom information.
"""

__author__ = "Arian Gallardo"
from models.user import User
from models.message import Message
from models.chatroom import Chatroom
from flask import request
from app import db
from resources.security import AuthRequiredResource
import status
import datetime
from flask_restful import Resource

class ChatroomResource(AuthRequiredResource):
    " Resource to manage individual chatroom information."
    def get(self, id):
        """ GET request handler for ChatroomResource. Reads chatroom
            information from the database with given chatroom id.

            In case of an error, HTTP status 400 (BAD_REQUEST) is returned.
            Else, HTTP status 200 (OK) is returned.
        """
        try:
            chatroom = Account.query.get_or_404(id)
            response = chatroom.to_json()
            return response, status.HTTP_200_OK
        except Exception as e:
            response = {"error": str(e)}
            return response, status.HTTP_400_BAD_REQUEST

class ChatroomListResource(Resource):
    " Resource to manage all chatrooms information."
    def get(self):
        """ GET request handler for ChatroomListResource. Reads chatroom
            information from the database for all the existing chatrooms.

            In case of an error, HTTP status 400 (BAD_REQUEST) is returned.
            Else, HTTP status 200 (OK) is returned.
        """
        try:
            chatrooms = Chatroom.query.all()
            response = {
                'chatrooms' : []
            }
            for chatroom in chatrooms:
                chatroom_dict = chatroom.to_json()
                response['chatrooms'].append(chatroom_dict)
            return response, status.HTTP_200_OK
        except Exception as e:
            response = {"error": str(e)}
            return response, status.HTTP_200_OK

    def put(self):
        """ PUT request handler for ChatroomListResource. Create a new
            chatroom given name and description.

            In case of an error, HTTP status 400 (BAD_REQUEST) is returned.
            Else, HTTP status 200 (OK) is returned.
        """
        try:
            request_dict = request.get_json()
            if not request_dict:
                response = {"error": "No input data provided."}
                return response, status.HTTP_400_BAD_REQUEST
            
            name = request_dict['name']
            description = (request_dict['description'] if 'description' in request_dict['description'] else "")

            chatroom = Chatroom(name=name, description=description)
            chatroom.add(chatroom)
            db.session.commit()

            response = {"ok": "Added chatroom successfully."}
            return response, status.HTTP_200_OK
        except Exception as e:
            response = {"error": str(e)}
            return response, status.HTTP_400_BAD_REQUEST